import sys
import r49_probe as r
all_cases=r.cases
def cases():return [c for c in all_cases() if any(x in c['id'] for x in ('ambiguity-free','select-parking-fee','watch-free','topic-reset','new-walk_in-1','new-personal_keyboard_mouse-1'))]
if __name__=='__main__':r.old.p.cases=cases;r.old.p.grade=r.grade;r.old.p.run(sys.argv[1],sys.argv[2])
