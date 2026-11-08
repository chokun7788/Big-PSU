from pathlib import Path
S=Path(__file__).resolve().parent/'r66_common_repair_20261014/system'
p=S/'app/knowledge/common/answer.py';t=p.read_text(encoding='utf-8')
old="                blocks.append('**'+title(r,lang)+'**\\n'+('This revision or a referenced record is not effective at the query time; no current fact is asserted.' if lang=='en' else 'ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้'))"
new="""                caption=title(r,lang)
                if r['kind']=='rate':
                    srv=records.get(value(r,'service_id'));aud=records.get(value(r,'audience_id'))
                    caption+=' — '+(title(srv,lang) if srv else '')+' / '+(title(aud,lang) if aud else '')
                interval=r['validity'];until=interval.get('effective_until');since=interval.get('effective_from')
                when=(' (recorded validity: '+str(since or '?')+' to '+str(until or '?')+')' if lang=='en' else ' (ช่วงมีผลที่บันทึก: '+str(since or '?')+' ถึง '+str(until or '?')+')') if since or until else ''
                blocks.append('**'+caption+'**\\n'+('This revision or a referenced record is not effective at the query time; no current fact is asserted.' if lang=='en' else 'ข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้')+when)"""
assert t.count(old)==1;t=t.replace(old,new);p.write_text(t,encoding='utf-8')
print('Source validity labels and scoped expired-price captions')
