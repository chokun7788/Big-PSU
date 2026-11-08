import json,collections,re,csv,hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r54_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
rows=json.loads((OUT/'responses.json').read_text())+json.loads((OUT/'extra_responses.json').read_text());pages=json.loads((OUT/'rule_pages.json').read_text())
notes={}
def assign(ids,status,note):
 for i in ids:notes[f'c{i:03}']=(status,note)
assign([9,43],'PASS_FORMAT','答案与owner source一致，只因83120后空格导致原始exact-match报警；忽略空白后通过。')
assign([18,45,46],'FAIL_INTENT','四人选择问题未匹配four_people；pattern只含four people/four of us和有限中文动作词，漏group of four/4 ppl/玩哪个等表达。应按owner回答Nintendo Switch。')
assign([19],'FAIL_TIMEOUT','未在deadline内回答。owner已给出named-player policy，实际只返回timeout；response无完整stage trace，不能确认是哪次模型调用耗时。')
assign([36,57],'FAIL_INTENT','休息座位有owner source，却未匹配rest_seating；英文被当游戏标题，中文返回泛化澄清。应回答中央休息区；不能据此确认特定booking等候点。')
assign([47],'PASS_EQUIVALENT','提问限定无名朋友代玩，答不可转让与该上下文的owner禁止条件一致；未评价其他有名队友的情况。')
assign([48,49],'FAIL_INTENT','证件问题有source，口语/拼错documents未进checkin_documents，而进入clarification/no_answer。')
assign([51],'SOURCE_REVIEW','旧rule source提供取消重订和至少1小时前、原slip；latest owner回答仅确认取消重订。答案主步骤相符，但source条件版本需协调，不能称为凭空编造。')
assign([54],'FAIL_WRONG_POLICY','错误slip应发Facebook page；却返回取消booking再重订旧rule。')
assign([56],'FAIL_WRONG_POLICY','代全组checkin应回答逐人检查/先到者可玩；却答一般checkin时间及证件。')
assign([61],'FAIL_FILTERS','request_plan把General adult及two hours丢失，customer_scope=unspecified、duration_minutes=null，回答全部人群每小时价格。应70×2=140 THB。')
assign([62,63],'FAIL_BUDGET','没有budget allocation路径。中文只报70/小时，英文What can I play触发games catalog，未按100baht筛选/算可负担session。PC General Adult100baht应1个60分钟package，余30baht（按记录价）。')
assign([64],'PASS_RECORDED','Nintendo3-4people generaladult记录价280/60min，正确标明原表到2026-03-31；本测试不确认现价续期。')
assign([71,72],'SAFE_UNCONFIRMED','正确不猜缺失的rental hours或不存在的PS55费率。')
assign([75,78],'FAIL_CATALOG','Nintendo/Cockpit游戏列表请求被当成未知游戏/没有答案；已存在按zone的catalog。')
assign([76,77],'PASS_CATALOG','命中正确zone游戏列表；不代表现场每台都安装/已更新。')
assign([80],'FAIL_AGGREGATE','ถามจำนวน游戏总数却检索到Naruto单条描述。应该从游戏catalog按去重口径计算并说明zone重复。')
assign([85],'PARTIAL_PAGE','CS2 full rules返回8/56部分，明确标记partial；target命中并不代表all coverage通过。后续分页另测失败。')
assign([88],'SAFE_EDITION','正确拒绝拿2026文档确认2030规则。')
assign([89,90,91,92,93,125],'LIVE_UNVERIFIED','WordPress live path有timestamp并返回closed/history状态，但未用同一timestamp外部ground truth逐slot比对；不等同availability accuracy确认。')
assign([94],'FAIL_TIME_ENTITY','VR紧跟9:00被_requested_resource_number的regex读成设备#9。不能把clock hour当机器编号。')
assign([95,96,98,99,100,101,102],'SAFE_UNCONFIRMED','针对未确认policy明确表示未知/区分旧recorded rule和owner未答项；不算wrong answer，不假定已解决owner policy。')
assign([97],'FAIL_UNHELPFUL_CLARIFICATION','Steam个人账号使用policy尚未确认；应明确该字段未知而非泛化询问游戏/价格/设备。')
assign([103,105,107,109,113,115],'PASS_CLARIFICATION','初轮价格缺service或比赛规则缺game，询问缺项合理；后续相同session返回选定scope。')
assign([111],'PASS_CATALOG','首轮PC游戏按设备组给出list。')
assign([112],'FAIL_CONTEXT','last_seen_response_id已提交；resolver仍用all_catalog_axis_ambiguous询问泛化scope，而非保留PC+games list。')
assign([117,119,121,123],'PASS_RECORDED','按对应记录source返回PC zone rental4000或PC generaladult70。')
assign([118],'PASS_RECORDED','followup继承PC rental并返回43 seats/10 PC units，正确区分座位容量与设备数量。')
assign([120],'SAFE_UNCONFIRMED','followup继承rental，但workbook没有rental booking流程，正确不借一般play booking替代。')
assign([124],'PASS_TARGET_ONLY','换话题至ROV后game/source正确，内容只选一条rule；仅确认topic不混PC价格，未认证overview覆盖全部。')
assign([126],'FAIL_CONTEXT','PC2 followup丢失前轮availability/日期/10点，no_matching_context_resolution，返回泛化clarification。')
extra={
127:('PASS_SCHEDULE','返回recorded timetable，未重新确认特殊关门。'),128:('FAIL_INTENT','opening hours被chatbot_identity_en拦截，回答自我介绍。'),
129:('GROUNDING_GAP','Maintenance属于中心schedule，却用了general LLM知识，未引用已有时段表；不能据此认定整天maintenance。'),
130:('PASS_SCHEDULE','recorded表列具体maintenance区间/午休/周末无常规服务，区分live。'),131:('FAIL_COVERAGE','问周日，仅返回周一到周五，未直接说明Sunday常规表未列服务。'),
132:('FAIL_COVERAGE','问where+when，只答地址，漏营业时间。'),133:('FAIL_OVERCLARIFICATION','booking流程完整问题被all/scope guard挡成询问全部哪个topic。'),
134:('PASS_RECORDED','返回6步booking流程及reservation source。'),135:('FAIL_COVERAGE','回答bank transfer，却没说明cash是否有确认，第二个问题未答。'),
136:('SAFE_UNCONFIRMED','cash许可未确认；generic no_answer虽不够友好，但不能按已有转账方法推出现金绝对禁止。'),
137:('FAIL_BUDGET','与c062同：只答单价不答可玩几轮。'),138:('FAIL_WRONG_POLICY','afford几session错误选择一次booking最多3session规则，与预算可负担数无关。'),
139:('DEVICE_VERIFY_PENDING','CS2shoot/reload从secondary guide回复LMB/R，明确设备设置未确认；不是现场验证通过。'),140:('FAIL_INTENT','CS2shoot/reload被当game availability，没回答buttons。'),
141:('SOURCE_QUALITY_ISSUE','Thai Tekken控制描述有Arabic بشكل，来自game_control_facts.jsonl原文并非本轮LLM生成；controls现场仍未验证。'),
142:('DEVICE_VERIFY_PENDING','English Tekken mappings返回已有secondary guide并注明设备未确认。'),143:('PASS_RECORDED','回答记录中的CPU/RAM/GPU；本轮未核对实际机器。'),
144:('FAIL_COVERAGE','问PC specifications，却只列equipment catalog，漏已有CPU/RAM/GPU。'),145:('FAIL_COVERAGE','membership+parking+ID只回答前两项，漏证件。'),
146:('PASS_MULTI_POLICY','英文3项都答出owner source。'),147:('PASS_MULTI_POLICY','中文2项正确分拆：personal mouse禁止+cancel/rebook机器。'),
148:('PASS_MULTI_POLICY','英文2项正确分拆：keyboard禁止+named-player条件。'),149:('LIVE_UNVERIFIED','明确时间隔开设备名可进live路径。09:00-09:30原区间及morning/afternoon两条输出，应再用fixture确认effective hour占用/套餐筛选，未认证可book。'),
150:('LIVE_UNVERIFIED','与c149同，英文输出已有booking历史，未独立验证有效时间/资源filter。'),151:('FAIL_MULTI_TARGET','PC1@10及PC2@11只回PC1@10，第二目标和时间被丢弃。'),
152:('FAIL_MULTI_FILTERS','games+2hours+generaladult只回price全部人群每package：漏games并丢word-number/group。'),153:('FAIL_MULTI_FILTERS','English同c152。'),
154:('PASS_OWNER','owner named-player policy直接正确。'),155:('FAIL_COVERAGE','问观看收费，只答允许观看。owner只确认permission，未确认费用，应说明费用未知。'),156:('SAFE_UNCONFIRMED','停车可用与免费不同，正确标明parking fees未指定。'),
}
for i,(s,n) in extra.items():assign([i],s,n)
unassigned=[]
for r in rows:
 c=r['case'];s,n=notes.get(c['id'],('PASS_BOUNDED','通过原始source/keyword检查，未据此声称所有claim/完整scope/当前数据已认证。'))
 if r.get('verdict')=='REVIEW' and c['id'] not in notes:unassigned.append(c['id'])
 r['analysis']={'status':s,'note':n,'reviewer':'agent_reading_source_and_actual_outputs_not_owner_confirmation','all_claims_verified':False}
assert not unassigned,unassigned
counts=collections.Counter(r['analysis']['status'] for r in rows);issues=[r for r in rows if r['analysis']['status'].startswith('FAIL') or r['analysis']['status'] in ('GROUNDING_GAP','SOURCE_QUALITY_ISSUE')]
lat=sorted(r['elapsed_sec'] for r in rows);p95=lat[int(.95*(len(lat)-1))]
summary=dict(cases=len(rows),language_counts=dict(collections.Counter(r['case']['locale'] for r in rows)),category_counts=dict(collections.Counter(r['case']['category'] for r in rows)),analysis_counts=dict(counts),observed_problem_cases=len(issues),transport_completed=sum(r['job'].get('status')=='completed' for r in rows),latency_median_sec=lat[len(lat)//2],latency_p95_sec=p95,latency_max_sec=max(lat),extra_rule_page_requests=len(pages['rows']),rule_page_summary=pages['summary'],scope='shop/service scenarios, sequential requests, not full corpus or concurrent load test',source_changed=False)
with (OUT/'analysis.json').open('x',encoding='utf-8') as s:json.dump({'summary':summary,'rows':rows},s,ensure_ascii=False,indent=2)
with (OUT/'case_index.csv').open('x',encoding='utf-8-sig',newline='') as s:
 writer=csv.writer(s);writer.writerow(['id','language','category','question','mode','seconds','status','note'])
 for r in rows:writer.writerow([r['case']['id'],r['case']['locale'],r['case']['category'],r['case']['question'],r['job']['result'].get('mode'),round(r['elapsed_sec'],3),r['analysis']['status'],r['analysis']['note']])
md='# คำถามและคำตอบจริงของชุดบริการ r54\n\n156 คำถาม + ตรวจ CS2 pagination เพิ่ม เก็บคำตอบทั้งหมดและlogเดิม คำอธิบายผลในanalysis.json/case_index.csv เป็นการอ่านวิเคราะห์ของagent ไม่ใช่การยืนยันนโยบายใหม่จากเจ้าของ คำอธิบายเชิงเทคนิคในตารางใช้ศัพท์อังกฤษ/จีนบางส่วน\n\n'
for r in rows:
 c=r['case'];answer=r['job']['result'].get('answer','');md+=f"## {c['id']}: {c['question']}\n\n- หมวด/ภาษา: {c['category']} / {c['locale']}\n- mode: {r['job']['result'].get('mode')}\n- เวลา: {r['elapsed_sec']:.2f}s\n- ผล: {r['analysis']['status']}\n- วิเคราะห์: {r['analysis']['note']}\n\n### คำตอบจริง\n\n{answer}\n\n"
with (OUT/'ALL_QUESTIONS_ANSWERS.md').open('x',encoding='utf-8') as s:s.write(md)
before=json.loads((OUT/'owner_hashes_before.json').read_text());changes=[p for p,h in before.items() if not(ROOT/p).exists() or hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h]
with (OUT/'owner_audit_after_all.json').open('x',encoding='utf-8') as s:json.dump({'checked':len(before),'changed':changes,'source_edited':False,'old_logs_deleted_or_overwritten':False},s,indent=2)
print(json.dumps(summary,ensure_ascii=False,indent=2))
