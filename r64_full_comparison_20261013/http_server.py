import os,sys
import harness
harness.init(os.environ['PSU_EVAL_FORMAT'],False)
from app.web_api.server import main
main()
