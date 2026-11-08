import os
import harness
harness.init('common',os.getenv('PSU_R66_LLM')=='1')
from app.web_api.server import main
if os.getenv('PSU_R66_TEST_DELIVERY_DELAY'):
 import time
 from app.session.conversation_store import STORE
 original_delivery=STORE.delivery
 def slow_delivery(*args,**kwargs):
  time.sleep(float(os.environ['PSU_R66_TEST_DELIVERY_DELAY']));return original_delivery(*args,**kwargs)
 STORE.delivery=slow_delivery
main()
