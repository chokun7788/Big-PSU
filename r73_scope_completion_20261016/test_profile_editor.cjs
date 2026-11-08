// Run the actual recursive owner-form widget with a minimal DOM adapter.
// This verifies form data handling, not browser layout or network transport.
const fs=require('fs'),vm=require('vm'),path=require('path');
const home=path.join(__dirname,'system/app/knowledge/common');
const source=fs.readFileSync(path.join(home,'ui/owner.js'),'utf8');
const start=source.indexOf('function defaults('),end=source.indexOf('function localTime(');
if(start<0||end<0)throw Error('Owner widget entry points not found');
class Element{
 constructor(tag,text){this.tag=tag;this.text=text;this.children=[];this.value='';this.options=[];}
 append(...items){this.children.push(...items);this.options.push(...items.filter(x=>x&&x.isOption));}
 setAttribute(){} addEventListener(){} remove(){}
}
const context={node:(t,s)=>new Element(t,s),Option:function(text,value){this.text=text;this.value=value;this.isOption=true;},dirty:false,status:{records:[]},SUB_LABELS:{},OPTION_LABELS:{},SIMPLE_FIELD_LABELS:{},FIELD_HELP:{faq:{},policy:{},procedure:{}}};
vm.createContext(context);vm.runInContext(source.slice(start,end),context);
const catalog=JSON.parse(fs.readFileSync(path.join(home,'catalog.json'),'utf8'));
const schema=catalog.find(x=>x.kind==='faq').fields.find(x=>x.key==='query_profile').value_schema;
const input={task:'permission',subjects:[{th:'อุปกรณ์ทดสอบ','en':'example controller'}],ownership:'personal',context:'studio'};
const widget=context.valueEditor(schema,input,null,'query_profile');
const got=widget.get();
if(JSON.stringify(got)!==JSON.stringify(input))throw Error('Profile widget changed entered values');
if(context.OPTION_LABELS.permission!=='ถามว่าใช้/นำมาได้ไหม')throw Error('Task labels missing');
if(!context.FIELD_HELP.procedure.query_profile.hint.includes('ไม่ต้องเขียนคำถามทุกแบบ'))throw Error('Profile help missing');
const result={passed:3,checks:['actual nested form widget round trip','human task labels','owner help/example'],scope:'actual owner form functions in minimal DOM, not real browser UI'};
fs.writeFileSync(path.join(__dirname,'PROFILE_EDITOR_QA.json'),JSON.stringify(result,null,2));process.stdout.write(JSON.stringify(result));
