import sys
import r45_regression as previous
old_cases=previous.final_cases
import r46_probe as current
current.prior.r.p.cases=lambda:old_cases()+current.cases()
if __name__=='__main__':current.prior.r.p.run(sys.argv[1],sys.argv[2])
