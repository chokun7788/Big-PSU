from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
tool=r'''"""Compare a saved aggregate snapshot with separately confirmed slot facts.
No network, booking writes, or inferred oracle values. Output JSON to stdout.
"""
import argparse,json,hashlib
from pathlib import Path
from datetime import datetime,timedelta

def compare(snapshot,oracle,snapshot_sha256):
    transport=oracle.get('transport',{})
    result={'transport_http_ok':transport.get('http_ok'), 'occupancy_verified':False,'grade':'pending','errors':[],'checked_slots':0}
    known=oracle.get('oracle',{})
    if oracle.get('collection_status')=='paused_by_user' or not known.get('observed_resources'):
        result['reason']='no_separately_confirmed_occupancy_oracle';return result
    if not known.get('confirmed_by') or known.get('source_snapshot_sha256')!=snapshot_sha256:
        result['errors'].append('unconfirmed_or_mismatched_snapshot');return result
    try:
        observed=datetime.fromisoformat(known['confirmed_at_bangkok'])
        if observed.utcoffset()!=timedelta(hours=7):raise ValueError('explicit Thai offset required')
    except (KeyError,ValueError,TypeError):
        result['errors'].append('missing_thai_confirmation_timestamp');return result
    if known.get('date')!=snapshot.get('date'):
        result['errors'].append('wrong_snapshot_date');result['grade']='failed';return result
    resources={str(r.get('resource_id')):r for r in snapshot.get('resources',[])}
    seen=set()
    for expected in known['observed_resources']:
        key=(str(expected.get('resource_id')),expected.get('start'),expected.get('end'))
        if key in seen:result['errors'].append('duplicate_oracle_slot:'+str(key));continue
        seen.add(key)
        if expected.get('expected_status') is None or not isinstance(expected.get('expected_available_count'),int):
            result['errors'].append('unconfirmed_slot:'+str(key));continue
        actual=next((s for s in resources.get(key[0],{}).get('slots',[]) if s.get('start')==key[1] and s.get('end')==key[2]),None)
        result['checked_slots']+=1
        if actual is None:result['errors'].append('missing_slot:'+str(key));continue
        if actual.get('status')!=expected['expected_status']:result['errors'].append('wrong_status:'+str(key))
        if actual.get('available_count')!=expected['expected_available_count']:result['errors'].append('wrong_available_count:'+str(key))
    result['grade']='failed' if result['errors'] else 'passed'
    result['occupancy_verified']=bool(result['checked_slots']) and not result['errors']
    result['scope']='Only listed confirmed slots in the exact saved snapshot; no claim for unlisted stations or future times.'
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--snapshot-json',type=Path,required=True);parser.add_argument('--oracle-json',type=Path,required=True)
    args=parser.parse_args();raw=args.snapshot_json.read_bytes();result=compare(json.loads(raw),json.loads(args.oracle_json.read_text(encoding='utf-8-sig')),hashlib.sha256(raw).hexdigest())
    print(json.dumps(result,ensure_ascii=False,indent=2));return 0 if result['grade']=='passed' else 2
if __name__=='__main__':raise SystemExit(main())
'''
(P/'tools/check_saved_booking_oracle_r32.py').write_text(tool,encoding='utf-8')
tests=r'''import unittest
from tools.check_saved_booking_oracle_r32 import compare
class SavedOracleTests(unittest.TestCase):
 def fixture(self):
  return {'date':'2026-10-01','resources':[{'resource_id':'1','slots':[{'start':'10:00','end':'11:00','status':'busy','available_count':0}]}]}, {'transport':{'http_ok':True},'collection_status':'confirmed_fixture','oracle':{'confirmed_by':'synthetic fixture','confirmed_at_bangkok':'2026-10-01T10:05:00+07:00','source_snapshot_sha256':'hash','date':'2026-10-01','observed_resources':[{'resource_id':'1','start':'10:00','end':'11:00','expected_status':'busy','expected_available_count':0}]}}
 def test_transport_success_without_real_oracle_is_pending(self):
  s,o=self.fixture();o['collection_status']='paused_by_user';r=compare(s,o,'hash');self.assertTrue(r['transport_http_ok']);self.assertFalse(r['occupancy_verified']);self.assertEqual(r['grade'],'pending')
 def test_separately_known_slot_passes(self):
  s,o=self.fixture();self.assertTrue(compare(s,o,'hash')['occupancy_verified'])
 def test_wrong_count_is_detected_despite_successful_transport(self):
  s,o=self.fixture();s['resources'][0]['slots'][0]['available_count']=1;r=compare(s,o,'hash');self.assertEqual(r['grade'],'failed');self.assertFalse(r['occupancy_verified'])
 def test_unbound_oracle_and_wrong_day_are_rejected(self):
  s,o=self.fixture();self.assertFalse(compare(s,o,'different')['occupancy_verified']);s['date']='2026-10-02';self.assertEqual(compare(s,o,'hash')['grade'],'failed')
 def test_timestamp_must_include_thai_offset(self):
  s,o=self.fixture();o['oracle']['confirmed_at_bangkok']='2026-10-01T10:05:00';self.assertFalse(compare(s,o,'hash')['occupancy_verified'])
'''
(P/'tests/test_saved_booking_oracle_r32.py').write_text(tests,encoding='utf-8')
print('added read-only saved-snapshot oracle checker and independent fixture tests')
