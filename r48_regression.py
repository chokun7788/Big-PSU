import sys
import r47_probe as old
import r48_probe as r
def grade(c,rs):
 if c['kind']=='location':
  return r.grade(dict(**c,key='location'),rs)
 return old.grade(c,rs)
if __name__=='__main__':
 r.p.OUT=r.OUT;r.p.cases=old.cases;r.p.grade=grade;r.p.run(sys.argv[1],sys.argv[2])
