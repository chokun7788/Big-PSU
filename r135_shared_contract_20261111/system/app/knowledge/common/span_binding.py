"""Bind harmless Unicode/case variants to original spans; never erase qualifiers."""
import unicodedata
def bind(question,quote):
    if not isinstance(quote,str) or not quote:return None
    text='';origins=[]
    for i,c in enumerate(question):
        for x in unicodedata.normalize('NFKC',c).casefold():text+=x;origins.append(i)
    target=unicodedata.normalize('NFKC',quote).casefold()
    start=text.find(target)
    if start<0:return None
    a,b=origins[start],origins[start+len(target)-1]+1
    return {'start':a,'end':b,'quote':question[a:b]}
