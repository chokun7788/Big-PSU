import sys
import r44_final_web as old
old_cases=old.cases
import r45_probe as new
new_cases=new.cases
def final_cases():
    compound='PC rental full day external organizations and VR rental half day internal organizations'
    return old_cases()+new_cases()+[
      dict(id='en-select-compound-child',locale='en',turns=[compound,'PC'],expected=new.r.expected(['pc'],['external'],['full_day'])),
      dict(id='en-resume-compound',locale='en',turns=[compound,'Competition rules for CS2','back to rental prices'],expected={**new.r.expected(['pc'],['external'],['full_day']),**new.r.expected(['vr'],['internal'],['half_day'])}),
      dict(id='en-expand-compound-catalog',locale='en',turns=[compound,'all rental rates'],expected=new.r.expected(new.r.ids)),
      dict(id='en-reject-all-periods',locale='en',turns=['PC rental price not half day and not full day'],expected={},missing=['scope_clarification']),
      dict(id='th-cancel-rental-prices',locale='th',turns=['ราคาเหมา PC หน่วยงานภายนอกครึ่งวัน','ไม่เอาราคาเหมาแล้ว'],negative=True),
    ]
new.r.p.cases=final_cases
if __name__=='__main__':new.r.p.run(sys.argv[1],sys.argv[2])
