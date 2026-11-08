"""Focused source-backed and adversarial checks; writes a new run directory."""
import os,sys,json,dataclasses,time,argparse
from pathlib import Path
from run_common import configure
R=Path(__file__).resolve().parent

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--tag',required=True);parser.add_argument('--llm',action='store_true');args=parser.parse_args()
    out=R/args.tag;out.mkdir(exist_ok=False);os.environ['PSU_R88_RUN_TAG']=args.tag;configure('focused')
    from app.pipeline.engine import answer_question_pipeline_debug
    from app.knowledge.common.dialogue import state_from_answer
    from app.knowledge.common.normalized_query import normalize_query
    from app.knowledge.common.task_contracts import TASKS
    from app.knowledge.common.registry import CATALOG
    from unittest.mock import patch
    checks=[]
    def check(name,ok,detail=None):
        row={'name':name,'passed':bool(ok),'detail':detail};checks.append(row)
        with (out/'CHECKS.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
        print(name,bool(ok),flush=True)
    def ask(q,locale='th',history=None):
        t=time.perf_counter()
        r=answer_question_pipeline_debug(q,locale=locale,experimental_rag_fallback=False,experimental_allow_llm=args.llm,global_timeout_sec=20,recent_history=history or [])
        row={'question':q,'locale':locale,'seconds':time.perf_counter()-t,'result':dataclasses.asdict(r)}
        with (out/'ANSWERS.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
        return r
    def history(q,r):return [{'role':'user','text':q},{'role':'assistant','text':r.answer,'common_read_state':state_from_answer(r),'delivery_status':'server_written'}]
    ctx=patch('urllib.request.urlopen',side_effect=AssertionError('Unexpected network in deterministic contract check')) if not args.llm else __import__('contextlib').nullcontext()
    with ctx:
        covered={k for t in TASKS.values() for k in t.kinds}
        check('Runtime task registry covers all schema kinds',set(CATALOG)<=covered,sorted(set(CATALOG)-covered))
        q='I am planning a visit and would like to know: What kind of game is Animal Crossing: New Horizons'
        r=ask(q,'en');check('English discourse does not veto exact game overview','Animal Crossing' in r.answer and r.validation.ok,r.answer[:500])
        r=ask('Could you please help me with this: Who operates PSU Esports Studio? Please use verified information','en')
        check('Source-backed university operator after shared framing','Prince of Songkla University' in r.answer and any(h.get('field')=='operator' for h in r.hits) and r.validation.ok,r.answer[:500])
        r=ask('จอสอบถามหน่อยครับ Sofa 2 seats คืออุปกรณ์อะไร')
        check('Typo polite prefix preserves exact equipment','Sofa 2 seats' in r.answer and r.validation.ok,r.answer[:500])
        r=ask('นายณัฐพนธ์ อินทรสังขนาวิน ทำตำแหน่งอะไร')
        check('Typed generic role regression has no exception',bool(r.answer) and r.validation.ok,r.answer[:350])
        r=ask('Please answer from verified studio informatiion: Which zone has the Gaming Monitor','en')
        check('Zone projection regression uses source zone','PC' in r.answer and r.validation.ok,r.answer[:350])
        r=ask('FINAL FANTASY XVI เล่นยงัไง')
        check('Previously fixed game how-to preserved','FINAL FANTASY' in r.answer and ('เนื้อเรื่อง' in r.answer or 'ภารกิจ' in r.answer),r.answer[:400])
        r=ask('Who are the studio members? Could you check this for me?','en')
        check('Public directory survives discourse','Manager' in r.answer and r.validation.ok,r.answer[:350])
        q='ต้องการทราบราคาบุคคลภายนอก';first=ask(q)
        r=ask('PC',history=history(q,first));check('Price choice PC retains pending subject','PC' in r.answer and 'เกม / อุปกรณ์' not in r.answer,r.answer[:400])
        r=ask('ทั้งหมด',history=history(q,first));check('All price services is not generic no-match','ยังระบุข้อมูลจากชุดที่ย้าย' not in r.answer,r.answer[:400])
        q='PC มีอะไรบ้าง';first=ask(q);r=ask('อุปกรณ์',history=history(q,first))
        check('Equipment follow-up remains scoped',bool(r.hits) and r.validation.ok,r.answer[:400])
        r=ask('วันนี้เปิดไหม');check('Day opening remains compact','ตารางเวลาบริการ' not in r.answer and len(r.answer)<450,r.answer)
        r=ask('นักศึกษาต่างมหาลัย เล่น VR 1 ชั่วโมง 30 นาที เสียกี่บาท')
        check('General student parser does not show adult rate','General Adult' not in r.answer,r.answer[:500])
        check('Expired price is not silently made current','หมดอายุ' in r.answer or 'ยังยืนยัน' in r.answer,r.answer[:500])
        q='PC11 ไม่เอา VR หลัง 13:00 เท่านั้น';n=normalize_query(q)
        check('Protected numbers and negation survive',all(x in n.text for x in ['pc11','ไม่เอา','13:00','หลัง']),n.public())
        check('Meaningful conjunction retained','and' in normalize_query('PC and VR price').text)
        check('Valid pay is not rewritten','pay' in normalize_query('How do I pay for PC?').text)
        for q in ['กฎ CS2 ต้องเล่นแบบ VALORANT ไหม','Can I bring my own food into the studio?','What is a mechanical keyboard like, short and not long?']:
            r=ask(q,'en' if q.isascii() else 'th');check('No exception / nonempty: '+q,bool(r.answer) and r.validation.ok,r.answer[:450])
    result={'checks':len(checks),'passed':sum(r['passed'] for r in checks),'failed':[r for r in checks if not r['passed']],'llm_enabled':args.llm,'scope':'Focused contracts, not full-system accuracy'}
    (out/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=False),flush=True)
    return 0 if not result['failed'] else 1
if __name__=='__main__':raise SystemExit(main())
