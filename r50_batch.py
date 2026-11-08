import sys
import r50_probe as r
import r48_variants as regression
if __name__=='__main__':
 for label,cases,grade in [('R50_FOCUSED_WEB',r.cases,r.grade),('R50_R49_WEB',r.old.cases,r.old.grade),('R50_R48_WEB',regression.cases,regression.grade)]:
  r.old.old.p.OUT=r.OUT;r.old.old.p.cases=cases;r.old.old.p.grade=grade;r.old.old.p.run(sys.argv[1],label)
