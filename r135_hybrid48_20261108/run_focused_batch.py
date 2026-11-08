"""One affected-regression batch; subprocess logs preserve every failure."""
import concurrent.futures,datetime,json,os,pathlib,subprocess,sys,time
R=pathlib.Path(__file__).resolve().parent
names=['verify_price_currency.py','verify_rate_calculation_receipt.py','verify_rate_person_bounds.py',
 'verify_exact_duration_receipts.py','verify_booking_payment_matrix.py','verify_raw_compounds.py',
 'verify_weekly_calendar.py','verify_calendar_windows.py','verify_contact_matrix.py',
 'verify_declared_phone_field.py','verify_direct_answer_20261105.py','verify_equipment_dimensions.py',
 'verify_person_scope.py','verify_news_matrix.py','verify_authority_projection.py',
 'verify_collection_contract.py','verify_terminal_delivery.py','verify_extended.py','verify_receipt_scope.py']
if len(sys.argv)>1:names=sys.argv[1:]
if (R/'FOCUSED_BATCH.json').exists():
    old=json.loads((R/'FOCUSED_BATCH.json').read_text('utf8'))
    (R/('FOCUSED_BATCH_HISTORY_'+str(time.time_ns())+'.json')).write_text(json.dumps(old,indent=2),'utf8')
out=R/('focused_batch_'+str(time.time_ns()));out.mkdir()
def run(name):
    start=time.time();p=subprocess.run([sys.executable,'-B',str(R/name)],capture_output=True,text=True,encoding='utf8',errors='replace',env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PYTHONUTF8':'1'},timeout=240)
    (out/(name+'.out.log')).write_text(p.stdout,'utf8');(out/(name+'.err.log')).write_text(p.stderr,'utf8')
    return {'script':name,'exit_code':p.returncode,'passed':p.returncode==0,'seconds':round(time.time()-start,2),'stdout':str(out/(name+'.out.log')),'stderr':str(out/(name+'.err.log'))}
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    futures={pool.submit(run,n):n for n in names}
    for f in concurrent.futures.as_completed(futures):
        try:row=f.result()
        except Exception as exc:row={'script':futures[f],'passed':False,'harness_error':repr(exc)}
        rows.append(row);report={'all_passed':all(x['passed'] for x in rows) and len(rows)==len(names),'completed':len(rows),'total':len(names),'rows':rows,'scope':'source-only focused checks, not semantic/production/whole-48 acceptance'}
        (R/'FOCUSED_BATCH.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps(row),flush=True)
sys.exit(0 if report['all_passed'] else 1)
