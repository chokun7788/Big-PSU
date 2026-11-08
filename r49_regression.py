import sys
import r48_variants as old
import r49_probe as r
if __name__=='__main__':r.old.p.OUT=r.OUT;r.old.p.cases=old.cases;r.old.p.grade=old.grade;r.old.p.run(sys.argv[1],sys.argv[2])
