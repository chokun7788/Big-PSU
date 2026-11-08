"""Bounded parent-process state; worker replacement does not replace dialogue."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import threading
import time
from collections import OrderedDict
from dataclasses import asdict, is_dataclass

from app.session.conversation_plan import resolve_request_plan, valid_price_task


class TurnConflict(ValueError):
    pass


class ConversationStore:
    def __init__(self, *, ttl=1800.0, max_sessions=512, clock=time.monotonic):
        self.ttl, self.max_sessions, self.clock = ttl, max_sessions, clock
        self._sessions = OrderedDict()
        self._guard = threading.RLock()

    def _record(self, session_id):
        now=self.clock()
        for key in list(self._sessions):
            if self._sessions[key]['expires'] <= now:
                del self._sessions[key]
        if session_id not in self._sessions:
            while len(self._sessions) >= self.max_sessions:
                self._sessions.popitem(last=False)
            self._sessions[session_id]={'revision':0,'active':None,'history':[],'turns':OrderedDict(),'expires':now+self.ttl}
        r=self._sessions[session_id]
        r['expires']=now+self.ttl
        self._sessions.move_to_end(session_id)
        return r

    def history(self, session_id, fallback=None):
        with self._guard:
            own=self._record(session_id)['history']
            if own:
                result = copy.deepcopy(own[-16:])
                deliveries = {t['response'].get('request_id'):t['delivery'] for t in self._sessions[session_id]['turns'].values() if t['response']}
                for item in result:
                    if item.get('role') == 'assistant':
                        item['delivery_status'] = deliveries.get(item.get('request_id'),'uncertain')
                return result
            if not isinstance(fallback,list):
                return []
            result = copy.deepcopy([r for r in fallback[-10:] if isinstance(r,dict) and r.get('role') in {'user','assistant'} and isinstance(r.get('text'),str) and len(r['text']) <= 16000])
            for item in result:
                item['delivery_status'] = 'uncertain'  # Client metadata cannot prove delivery.
            return result

    def begin(self, session_id, turn_id, question, *, locale='th', history=None):
        fingerprint=hashlib.sha256(json.dumps([question,locale],ensure_ascii=False).encode()).hexdigest()
        with self._guard:
            r=self._record(session_id)
            old=r['turns'].get(turn_id)
            if old:
                if old['fingerprint'] != fingerprint:
                    raise TurnConflict('client_turn_id was reused for a different question or language')
                if old['response'] is None and old['revision'] != r['revision']:
                    raise TurnConflict('pending turn is older than the active state revision')
                return copy.deepcopy(old)
            plan=resolve_request_plan(question,history,active_task=r['active'],locale=locale)
            r['revision']+=1
            if plan and plan.get('tasks') and valid_price_task(plan['tasks'][0]):
                r['active']=copy.deepcopy(plan['tasks'][0])
            else:
                # An explicit topic shift is committed even when its tool fails.
                r['active']=None
            turn={'fingerprint':fingerprint,'revision':r['revision'],'question':question,'plan':plan,'response':None,'delivery':'prepared'}
            r['turns'][turn_id]=turn
            while len(r['turns'])>8:
                r['turns'].popitem(last=False)
            return copy.deepcopy(turn)

    def complete(self, session_id, turn_id, revision, response, *, plan=None):
        with self._guard:
            r=self._record(session_id)
            turn=r['turns'].get(turn_id)
            if not turn or r['revision'] != revision:
                return False
            if plan and plan.get('tasks') and valid_price_task(plan['tasks'][0]):
                r['active']=copy.deepcopy(plan['tasks'][0])
                turn['plan']=copy.deepcopy(plan)
            if response.get('ok'):
                turn['response']=copy.deepcopy(response)
                intent=response.get('universal_intent')
                if is_dataclass(intent):
                    intent=asdict(intent)
                r['history'].extend([
                    {'role':'user','text':turn['question']},
                    {'role':'assistant','text':response.get('answer',''),'route_category':response.get('route_category',''),
                     'route_intent':response.get('route_intent',''),'resolved_text':(turn['plan'] or {}).get('resolved_query',response.get('resolved_question',turn['question'])),
                     'universal_intent':intent,'request_plan':turn['plan'],'request_id':response.get('request_id',''),
                     'rule_coverage':copy.deepcopy(response.get('rule_coverage'))},
                ])
                r['history']=r['history'][-16:]
            return True

    def delivery(self, session_id, turn_id, status):
        if status not in {'server_written','uncertain'}:
            raise ValueError('invalid delivery status')
        with self._guard:
            turn=self._record(session_id)['turns'].get(turn_id)
            if turn and turn['delivery'] != 'client_acknowledged':
                turn['delivery']=status

    def acknowledge(self, session_id, response_id):
        with self._guard:
            for turn in self._record(session_id)['turns'].values():
                if turn['response'] and turn['response'].get('request_id')==response_id:
                    turn['delivery']='client_acknowledged'
                    return True
        return False

    def snapshot(self, session_id):
        with self._guard:
            r=self._record(session_id)
            return {'schema_version':1,'revision':r['revision'],'active_task':copy.deepcopy(r['active']),
                    'delivery':{k:t['delivery'] for k,t in r['turns'].items()},'storage':'parent_memory','survives_server_restart':False}


STORE = ConversationStore(ttl=max(60,float(os.getenv('PSU_CONVERSATION_TTL_SEC','1800'))), max_sessions=max(1,int(os.getenv('PSU_CONVERSATION_MAX_SESSIONS','512'))))
