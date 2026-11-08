from pathlib import Path
R=Path(__file__).resolve().parent
x=(R/'finish_experiment.py').read_text('utf8').replace("OUT=R/'execution01'","OUT=R/'execution02'")
x=x.replace("assert health['pid']==server.pid and health['training_complete_verified'];break", "assert (health['pid']==server.pid or server.pid in [p.pid for p in psutil.Process(health['pid']).parents()]) and health['training_complete_verified'];break")
x=x.replace("server.terminate()\n  try:server.wait(timeout=15)\n  except subprocess.TimeoutExpired:server.kill();server.wait(timeout=5)", """# The Windows venv launcher can have a real interpreter child. Stop only
  # this supervisor's own server tree; otherwise the GPU process could remain.
  try:children=psutil.Process(server.pid).children(recursive=True)
  except psutil.NoSuchProcess:children=[]
  for child in reversed(children):
   try:child.terminate()
   except psutil.NoSuchProcess:pass
  server.terminate()
  try:server.wait(timeout=15)
  except subprocess.TimeoutExpired:server.kill();server.wait(timeout=5)""")
target=R/'finish_experiment02.py';assert not target.exists();target.write_text(x,'utf8')
print('Prepared own-process-aware execution supervisor')
