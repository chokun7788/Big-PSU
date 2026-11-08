"""Reuse a targeted suite with candidate overlay and isolated new outputs."""
import json,runpy,sys,urllib.request
from pathlib import Path
from unittest.mock import patch
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016'
script=Path(sys.argv[1]).resolve();tag=sys.argv[2]
output=B/'verification'/tag
sys.path.insert(0,str(S/'system'));sys.path.insert(0,str(script.parent))
import app.knowledge.common as pkg
pkg.__path__.insert(0,str(B/'candidate/app/knowledge/common'))
sys.argv=[str(script),str(output),str(S)]
# Existing suites replace this for their controlled output tests as needed.
# Any other attempted network is an explicit fixture failure, not a real call.
with patch.object(urllib.request,'urlopen',side_effect=OSError('R81 CONTROLLED unavailable model transport')):
    runpy.run_path(str(script),run_name='__main__')
