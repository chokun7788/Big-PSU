import copy, json, sys, time, urllib.request
from r27_fixture import PROJECT, REPORT, check
sys.path.insert(0,str(PROJECT))
from app.pipeline.engine import answer_question_pipeline_debug

# New phrasings fixed before their first execution. These are constructed
# development/regression cases; after inspection they are not labelled blind.
PAIRS=[
('cs2-protest','ตามกติกาการแข่งขัน CS2 โค้ชขอยื่นประท้วงหลังจบแมตช์ได้ภายในเวลาเท่าไร','Under CS2 tournament rules, what deadline applies when a coach submits a protest after the match?','ประท้วง','protest'),
('cs2-notes','ตามกติกาการแข่งขัน CS2 หัวหน้าทีมนำโน้ตเข้าไปแล้วต้องให้กรรมการตอนไหน','Under CS2 tournament rules, when must the team leader hand notes to the referee?','โน้ต','notes'),
('cs2-social-exception','ตามกติกาการแข่งขัน CS2 เปิดโซเชียลบนคอมแข่งขันมีข้อยกเว้นอะไร','Under CS2 tournament rules, what exception applies to social media access?','โซเชียล','social'),
('cs2-provided','ตามกติกาการแข่งขัน CS2 อุปกรณ์ที่ผู้จัดเตรียมให้มีอะไร','Under CS2 tournament rules, list the equipment that organizers provide.','อุปกรณ์','equipment'),
('cs2-own-gear','ตามกติกาการแข่งขัน CS2 อุปกรณ์ของตัวเองที่เอาเข้าแข่งได้มีอะไร','Under CS2 tournament rules, what own equipment can competitors bring?','อุปกรณ์','equipment'),
('cs2-timer','ตามกติกาการแข่งขัน CS2 Freeze time กับเวลาต่อรอบกำหนดไว้เท่าไร','Under CS2 tournament rules, specify Freeze time and round time.','กติกา','rules'),
('cs2-roster-change','ตามกติกาการแข่งขัน CS2 เปลี่ยนสมาชิกทีมหลังเริ่มรายการได้หรือไม่','Under CS2 tournament rules, are team member changes permitted during the event?','กติกา','rules'),
('rov-rematch','ตามกติกาการแข่งขัน RoV First Blood มาแล้วสามารถขอเริ่มเกมใหม่ได้หรือไม่ และถ้ายังไม่มีล่ะ','Under RoV tournament rules, contrast restart requests before and after First Blood.','กติกา','rules'),
('rov-heroes','ตามกติกาการแข่งขัน RoV ฮีโร่ที่ต้องมีอย่างน้อยกำหนดกี่ตัว','Under RoV tournament rules, what is the minimum number of heroes required?','ฮีโร่','heroes'),
('rov-overheat','ตามกติกาการแข่งขัน RoV ถ้าเครื่องร้อนจนเฟรมลด กรรมการให้หยุดได้นานเท่าไร','Under RoV tournament rules, how long may staff pause for overheating and what condition applies?','กติกา','rules'),
('tekken8-assist','ตามกติกาการแข่งขัน Tekken 8 ระบบช่วยเหลือพิเศษหรือปุ่ม Assist ใช้ได้หรือเปล่า','Under Tekken 8 tournament rules, is the special Assist system allowed?','กติกา','rules'),
('tekken8-settings','ตามกติกาการแข่งขัน Tekken 8 การตั้งค่าเกมต้องใช้ Round Timer Advantage Stage แบบไหน','Under Tekken 8 tournament rules, list all in-game settings including Stage and Advantage.','การตั้งค่า','settings'),
('valorant-kayo','ตามกติกาการแข่งขัน VALORANT KAY/O ใช้ ZERO/POINT นอกแผนที่ได้แค่ไหน','Under VALORANT tournament rules, what conditions apply to the KAY/O ZERO/POINT exception?','กติกา','rules'),
('valorant-forfeit-score','ตามกติกาการแข่งขัน VALORANT ถ้าปรับแพ้แผนที่ บันทึกคะแนนเป็นอะไร','Under VALORANT tournament rules, what score is recorded for a map forfeit?','คะแนน','score'),
('valorant-new-content','ตามกติกาการแข่งขัน VALORANT เอเจนท์ใหม่กับแผนที่ใหม่จำกัดการใช้กี่สัปดาห์','Under VALORANT tournament rules, how long must new agents and new maps remain restricted?','กติกา','rules'),
('valorant-rollback','ตามกติกาการแข่งขัน VALORANT มีดาเมจแล้วกับยังไม่มีดาเมจ ย้อนรอบได้อย่างไร','Under VALORANT tournament rules, explain when officials may roll back before and after damage.','กติกา','rules'),
]

def build():
    source=json.loads((REPORT/'content_contract_fixture_v2.json').read_text(encoding='utf-8'))['cases']
    anchors={c['anchor']:c for c in source if c['mutation']=='clean'}
    cases=[]
    for key,th,en,thword,enword in PAIRS:
        for locale,clean,word in [('th',th,thword),('en',en,enword)]:
            base=anchors[key+'-'+locale]
            dup=clean.replace('กติกา','กติกกา',1) if locale=='th' else clean.replace('tournament','tournamment',1)
            multi=dup.replace('แข่งขัน','แข่่งขัน',1) if locale=='th' else dup.replace('rules','ruls',1)
            omission=clean.replace(word,word[:len(word)//2]+word[len(word)//2+1:],1)
            for n,q in enumerate([clean,dup,multi,omission]):
                case=copy.deepcopy(base);case.update(id=f'R27-new-{key}-{locale}-{n}',question=q,mutation=['new_clean','task_duplication','two_task_errors','facet_deletion'][n])
                cases.append(case)
    return cases

if __name__=='__main__':
    run=sys.argv[1];port=sys.argv[2] if len(sys.argv)>2 else None
    path=REPORT/'new_questions_fixture_128.json'
    if not path.exists():
        with path.open('x',encoding='utf-8') as f:json.dump(build(),f,ensure_ascii=False,indent=2)
    cases=json.loads(path.read_text(encoding='utf-8'));records=[]
    with (REPORT/(run+'_details.jsonl')).open('x',encoding='utf-8') as out:
        for case in cases:
            start=time.perf_counter()
            if port:
                payload={'question':case['question'],'locale':case['locale'],'recent_history':[],'experimental_allow_llm':True,'experimental_rag_fallback':True,'debug':True}
                raw=json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:'+port+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=25))
                response={'answer':raw['answer'],'mode':raw['mode'],'category':raw['route_category'],'hits':raw.get('sources',[]),'valid':raw.get('validation_ok',True),'raw':raw}
            else:
                result=answer_question_pipeline_debug(case['question'],locale=case['locale'],experimental_allow_llm=False,experimental_rag_fallback=True,global_timeout_sec=20)
                response={'answer':result.answer,'mode':result.mode,'category':result.route.category,'hits':result.hits,'valid':result.validation.ok,'trace':[vars(t) for t in result.trace]}
            failures=check(case,response)
            r={'id':case['id'],'anchor':case['anchor'],'question':case['question'],'locale':case['locale'],'mutation':case['mutation'],'elapsed':round(time.perf_counter()-start,4),'failures':failures,'passed':not failures,'response':response};records.append(r);out.write(json.dumps(r,ensure_ascii=False)+'\n');out.flush()
    summary={'total':len(records),'passed':sum(r['passed'] for r in records),'failed_anchors':sorted({r['anchor'] for r in records if not r['passed']}),'max_elapsed':max(r['elapsed'] for r in records),'port':port,'review':'constructed new development cases; not blind user traffic'}
    with (REPORT/(run+'_summary.json')).open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
    print(json.dumps(summary,ensure_ascii=False),flush=True)
