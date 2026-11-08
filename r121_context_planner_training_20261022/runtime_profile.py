"""One explicit model profile for every native caller, including old fallbacks."""
MODEL_VARIABLES=('PSU_CHATBOT_OLLAMA_MODEL','PSU_KNOWLEDGE_LLM_MODEL','PSU_QUERY_PLANNER_MODEL','PSU_TOOL_ROUTER_MODEL','PSU_INTENT_LLM_MODEL')
def profile_environment(profile,endpoint='http://127.0.0.1:12121'):
 if profile not in {'psu-r121-base:latest','psu-r121-trained:latest'}:raise ValueError('Unknown experimental model profile')
 return {'OLLAMA_URL':endpoint,**{name:profile for name in MODEL_VARIABLES}}
