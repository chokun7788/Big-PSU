import faulthandler,cProfile,pstats,time
import harness
faulthandler.dump_traceback_later(8,repeat=True)
harness.init('common',False)
prof=cProfile.Profile();prof.enable();start=time.perf_counter()
r,_,_,elapsed=harness.run({'question':'กฎตอนแข่ง cs2 มีอะไรมั่ง','locale':'th','reference_date':''})
prof.disable();faulthandler.cancel_dump_traceback_later()
print(r.mode,elapsed,r.answer[:1200],flush=True);pstats.Stats(prof).sort_stats('cumulative').print_stats(18)
