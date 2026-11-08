from pathlib import Path
S=Path(__file__).resolve().parent/'r66_common_repair_20261014/system'
p=S/'app/knowledge/common/answer.py';t=p.read_text(encoding='utf-8')
old="    def answer(self,question,*,locale='th',history=None,at=None,planner=None):";assert t.count(old)==1;t=t.replace(old,"    def answer(self,question,*,locale='th',history=None,at=None,planner=None,_composing=False):")
old="        matched_ids=list(ids)";assert t.count(old)==1;t=t.replace(old,"        if not _composing:\n            from .composition import parts,compose\n            clauses=parts(strip_names(question,ids,names))\n            if clauses and ids:return compose(self,snap,started,clauses,ids,lang=lang,history=history,at=at,planner=planner)\n        matched_ids=list(ids)")
p.write_text(t,encoding='utf-8');print('bounded compound operation coverage')
