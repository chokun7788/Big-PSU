import sys
import r44_probe as r
import r44_extra as e
base_cases=r.cases
def cases():
    cs=base_cases()+e.cases()
    cs+= [
      dict(id='en-unknown-suffix',locale='en',turns=['Rental price for Xbox full day'],expected={},missing=['unresolved_targets']),
      dict(id='en-unknown-after-group',locale='en',turns=['Rental price for external organizations for Xbox'],expected={},missing=['unresolved_targets']),
      dict(id='th-group-shorthand',locale='th',turns=['ราคาเหมา PC หน่วยงานนอกครึ่งวัน'],expected=r.expected(['pc'],['external'],['half_day'])),
      dict(id='en-internal-prefix',locale='en',turns=['PSU department PC rental price half day'],expected=r.expected(['pc'],['internal'],['half_day'])),
      dict(id='en-student-prefix',locale='en',turns=['PSU student PC rental price'],expected=r.expected(['pc']),missing=['eligibility']),
      dict(id='en-venue-location',locale='en',turns=['Where is the venue?'],negative=True),
      dict(id='en-venue-hours',locale='en',turns=['What are the venue opening hours?'],negative=True),
    ]
    return cs
r.p.cases=cases
if __name__=='__main__':r.p.run(sys.argv[1],sys.argv[2])
