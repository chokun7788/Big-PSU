import json,hashlib,re
from r28_fixture import REPORT,PROJECT,clauses,approved_localization,BOOKS
data=json.loads((REPORT/'composition_fixture_v1.json').read_text(encoding='utf-8'))
rows={x['id']:x for x in [json.loads(s) for s in (PROJECT/'data/competition_rules/competition_rule_chunks.jsonl').read_text(encoding='utf-8').splitlines()]}
extras=[
('money-regular-overtime','กติกา CS2 เงินเริ่มต้นและเวลาระเบิดรอบปกติเท่าไร แล้วต่อเวลามีกี่รอบและเงินเริ่มต้นเท่าไร','Under CS2 tournament rules, what are starting money and bomb time in regulation, and what are overtime rounds and starting money?',[('25',r'เงินเริ่มต้น',r'Initial money'),('27',r'การต่อเวลา',r'Overtime:')]),
('language-protest','กติกา CS2 ประท้วงใช้ภาษาอะไร ใครยื่นและภายในกี่นาที','Under CS2 tournament rules, which language must protests use, who may file a protest and within how many minutes?',[('06',r'ภาษา ภาษาทางการ',r'Language:'),('58',r'การประท้วง ต้องยื่น',r'Protests must')]),
('gear-bring-quality','กติกา CS2 นำอุปกรณ์ของตัวเองอะไรมาได้ แล้วใครรับผิดชอบคุณภาพและความพร้อมของอุปกรณ์','Under CS2 tournament rules, what personal equipment may I bring and who is responsible for its quality and readiness?',[('41',r'นำคีย์บอร์ด',r'Players may bring'),('42',r'รับผิดชอบ',r'responsible')]),
('maps-pool-tool','กติกา CS2 ใช้แผนที่อะไรบ้าง แล้วเลือกแผนที่ผ่านเว็บอะไร','Under CS2 tournament rules, which maps are used and which website is used for map selection?',[('29',r'ANCIENT',r'ANCIENT'),('31',r'MAPBAN',r'MAPBAN')]),
]
extra=[]
for key,th,en,requirements in extras:
    for locale,q in [('th',th),('en',en)]:
        required=[];sources=[];hashes={}
        for section,thpattern,enpattern in requirements:
            sid='competition_rules_cs2_psu_phuket_2026_s'+section+'_c01';row=rows[sid]
            text=row['text'] if locale=='th' else approved_localization(row,'text')
            match=[c for c in clauses(text) if re.search(thpattern if locale=='th' else enpattern,c,re.I)]
            assert match,(key,locale,text)
            required+=match;sources.append(sid);hashes[sid]=hashlib.sha256(row['text'].encode('utf-8')).hexdigest()
        for n,(mutation,question) in enumerate([('clean',q),('polite','สอบถามหน่อยครับ '+q+' ครับ' if locale=='th' else 'Could you help me? '+q),('task-typo',q.replace('กติกา','กติกกา') if locale=='th' else q.replace('tournament','tournamment').replace('rules','ruls'))]):
            extra.append({'id':f'R28-{key}-{locale}-{n}','anchor':key,'locale':locale,'kind':'composite','mutation':mutation,'question':question,'game':'cs2','sources':sources,'source_sha256':hashes,'clauses':required,'status':'answer'})
data['cases']+=extra;data['anchor_count']+=4;data['composite_anchors']+=4
with (REPORT/'composition_fixture_v2.json').open('x',encoding='utf-8') as f:json.dump(data,f,ensure_ascii=False,indent=2)
with (REPORT/'additional_baseline_fixture_24.json').open('x',encoding='utf-8') as f:json.dump(dict(data,cases=extra),f,ensure_ascii=False,indent=2)
print(len(data['cases']))
