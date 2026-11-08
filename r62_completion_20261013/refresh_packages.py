from pathlib import Path
import shutil
from package_r62 import B,SYSTEM,OUT,tree
for root in OUT.iterdir():
 if not root.is_dir():continue
 tree(SYSTEM/'app',root/'app');tree(SYSTEM/'web_chat',root/'web_chat')
 for p in SYSTEM.iterdir():
  if p.is_file() and p.suffix in {'.ps1','.cmd','.md'} or p.name=='Model-Manifest-Check.py':shutil.copy2(p,root/p.name)
 shutil.copy2(B.parent/'r61_implementation_20261013/OWNER_REVIEW_PACKET.md',root/'OWNER_REVIEW_PENDING.md')
print('Updated both new delivery packages without replacing their databases or model blobs.')
