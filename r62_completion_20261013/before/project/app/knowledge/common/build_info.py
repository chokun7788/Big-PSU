"""Fingerprint captured at module load; never includes databases or tokens."""
from pathlib import Path
import hashlib
def _capture():
 home=Path(__file__).resolve().parent;digest=hashlib.sha256()
 for p in sorted(home.iterdir()):
  if p.suffix not in {'.py','.json'}:continue
  digest.update(p.name.encode());digest.update(p.read_bytes())
 return {'build_id':'common-r61','loaded_source_sha256':digest.hexdigest(),'fingerprint_scope':'common Python and developer metadata at module import'}
LOADED_BUILD=_capture()
