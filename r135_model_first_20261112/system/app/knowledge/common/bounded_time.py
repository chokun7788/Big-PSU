"""Cooperative analysis budget; does not certify a hard wall-clock deadline."""
import os,time
def number(name,default):
 try:return max(0.0,float(os.getenv(name,str(default))))
 except ValueError:return default
def remaining():
 from .flow_context import CURRENT
 ctx=CURRENT.get()
 return max(0.0,number('PSU_ANALYSIS_BUDGET_SEC',20)-(time.perf_counter()-ctx.started)) if ctx else None
def timeout(requested):
 left=remaining();limit=min(float(requested),number('PSU_ANALYSIS_CALL_SEC',5))
 return max(0.0,min(limit,left)) if left is not None else max(0.0,limit)
def exhausted():
 left=remaining();return left is not None and left<=0
