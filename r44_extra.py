import sys
import r44_probe as r
def cases():
    cs=[]
    for lang in ('th','en'):
        en=lang=='en'
        for name,q,missing,rates in [
          ('hourly-rental','What is the hourly PC rental price?' if en else 'ราคาเหมา PC รายชั่วโมง',['hourly_rental'],{}),
          ('multi-day','PC rental price for 3 days' if en else 'ราคาเหมา PC 3 วัน',['multi_day'],r.expected(['pc'])),
          ('staff','PC rental staff overtime extra charge' if en else 'เช่าโซน PC มีค่าเจ้าหน้าที่นอกเวลาเท่าไหร่',['overtime'],{}),
          ('rental-live','Is PC rental available now?' if en else 'เหมา PC ว่างไหมตอนนี้',['live_availability'],{}),
          ('direct-rent','Rent PC full day' if en else 'เช่า PC เต็มวัน',[],r.expected(['pc'],periods=['full_day'])),
          ('exclude','Show all rental rates except PC' if en else 'ขอราคาเหมาทุกแพ็กเกจยกเว้น PC',[],r.expected([t for t in r.ids if t!='pc'])),
        ]:cs.append(dict(id=f'{lang}-{name}',locale=lang,turns=[q],expected=rates,missing=missing))
        cs.append(dict(id=f'{lang}-both-groups',locale=lang,turns=['PC rental price for external organizations' if en else 'ราคาเหมา PC หน่วยงานภายนอก','both groups' if en else 'ทั้งสองกลุ่ม'],expected=r.expected(['pc'])))
        cs.append(dict(id=f'{lang}-included-followup',locale=lang,turns=['PC rental price' if en else 'ราคาเหมา PC','What is included?' if en else 'รวมอะไรบ้าง'],expected={},required=['10']))
    return cs
r.p.cases=cases
if __name__=='__main__':r.p.run(sys.argv[1],sys.argv[2])
