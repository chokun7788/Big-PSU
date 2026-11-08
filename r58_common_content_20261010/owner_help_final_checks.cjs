// Focused UI serialization tests. No browser automation or production database writes.
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const p=require('./owner_help_latest.json'),root=p.stage,source=fs.readFileSync(root+'/owner.js','utf8');
class Element{constructor(tag){this.tag=tag;this.children=[];this.value='';this.options=[];}append(...xs){this.children.push(...xs);if(this.tag==='select')this.options.push(...xs);}setAttribute(){}addEventListener(){}remove(){} }
const context=vm.createContext({node:t=>new Element(t),Option:class {constructor(text,value){this.text=text;this.value=value;}},status:{records:[]},SUB_LABELS:{},OPTION_LABELS:{},dirty:false});
vm.runInContext(source.slice(source.indexOf('function valueEditor('),source.indexOf('function localTime(')),context);
function editor(v,key='amount_minor'){return context.valueEditor({type:'integer',minimum:0},v,null,key);}
const cases=[];
function check(name,fn){fn();cases.push({name,passed:true});}
for(const [input,expected] of [['35',3500],['35.50',3550],['35.5',3550],['4,000',400000],['0',0],['0.01',1],[' 70.00 ',7000]])check('baht '+input,()=>{let e=editor(null);e.root.children[0].value=input;assert.equal(e.get(),expected);});
for(const input of ['', '-1','35.555','3,5','35,50','1e3','NaN','Infinity','999999999999999999999'])check('reject '+input,()=>{let e=editor(null);e.root.children[0].value=input;assert.throws(()=>e.get());});
for(const minor of [0,1,3500,3550,400000,123456789])check('existing price '+minor,()=>{let e=editor(minor);assert.equal(e.get(),minor);});
check('unknown price input blank',()=>assert.equal(editor(null).root.children[0].value,''));
check('weekday retained',()=>{let e=editor(6,'weekday');assert.equal(e.get(),6);});
check('weekday Thai labels',()=>assert.equal(editor(0,'weekday').root.children[0].options[0].text,'จันทร์'));
fs.writeFileSync(p.run+'/serialization_checks.json',JSON.stringify({total:cases.length,passed:cases.length,cases},null,2));
console.log(JSON.stringify({total:cases.length,passed:cases.length}));
