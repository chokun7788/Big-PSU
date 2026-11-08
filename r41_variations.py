import sys
import r41_probe as probe

def cases():
    rows=[]
    for lang in ('th','en'):
        en=lang=='en'
        controls='Show me the game controls' if en else 'ขอดูปุ่มควบคุมเกม'
        rules='Competition rules for CS2' if en else 'กฎการแข่งขัน CS2'
        price='PC prices for external users' if en else 'ราคา PC ของบุคคลภายนอก'
        rows += [
            dict(id=lang+'-partial-all',locale=lang,turns=[controls,'VALORANT and Minecraft' if en else 'VALORANT กับ มายคราฟต์','all of them' if en else 'ทั้งหมด'],kind='partial',required=['VALORANT']),
            dict(id=lang+'-multi-all',locale=lang,turns=[controls,'VALORANT and Beat Saber' if en else 'VALORANT กับ Beat Saber','all of them please' if en else 'ทั้งหมดเลยครับ'],kind='complete_multi',required=['VALORANT','Beat Saber']),
            dict(id=lang+'-multi-resume',locale=lang,turns=[controls,'VALORANT and Beat Saber' if en else 'VALORANT กับ Beat Saber',price,'return to the controls' if en else 'กลับไปเรื่องปุ่มเดิม'],kind='complete_multi',required=['VALORANT','Beat Saber']),
            dict(id=lang+'-family-second',locale=lang,turns=['Call of Duty controls' if en else 'Call of Duty มีปุ่มอะไรบ้าง','the second one' if en else 'อันที่สอง'],kind='controls',required=['Call of Duty: Warzone'],forbidden=['Modern Warfare III controls:']),
            dict(id=lang+'-typo-then-all',locale=lang,turns=['Valoant controls' if en else 'Valoant มีปุ่มอะไรบ้าง','everything' if en else 'ทุกอัน'],kind='controls',required=['VALORANT']),
            dict(id=lang+'-catalog-multi-resume',locale=lang,turns=['What games can I play?' if en else 'มีเกมอะไรให้เล่นบ้าง','PC and PS5' if en else 'PC กับ PS5',rules,'back to the game list' if en else 'กลับไปรายชื่อเกมเมื่อกี้'],kind='catalog',required=['PC Zone','PlayStation 5 Zone'],forbidden=['VR Zone','Cockpit Zone','Nintendo Switch Zone']),
            dict(id=lang+'-unknown-cannot-revert',locale=lang,turns=['VALORANT controls' if en else 'VALORANT มีปุ่มอะไรบ้าง','Minecraft controls' if en else 'Minecraft มีปุ่มอะไรบ้าง','all of them' if en else 'ทั้งหมด'],kind='clarification',forbidden=['VALORANT controls:']),
            dict(id=lang+'-unresolved-return-filter',locale=lang,turns=[price,rules,'back to the prices for tomorrow' if en else 'กลับไปเรื่องราคาของพรุ่งนี้'],kind='clarification'),
            dict(id=lang+'-explicit-return-new-target',locale=lang,turns=['VALORANT controls' if en else 'VALORANT มีปุ่มอะไรบ้าง',price,'back to controls for Beat Saber' if en else 'กลับไปดูปุ่ม Beat Saber'],kind='controls',required=['Beat Saber'],forbidden=['VALORANT controls:']),
        ]
    return rows

probe.cases=cases
if __name__=='__main__':probe.run(sys.argv[1],sys.argv[2])
