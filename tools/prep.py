import json, sys
src = sys.argv[1]
L = lambda f: json.load(open(f"{src}/{f}", encoding='utf-8'))
items, bosses, skills, heros = L('items.json'), L('bosses.json'), L('skills-boss.json'), L('heros.json')
icons = set(open(sys.argv[2]).read().split('\n'))
out_items = []
for i in items:
    st = i.get('stats') or {}
    if isinstance(st.get('active'), str): st['active'] = [st['active']]
    d = {k: i[k] for k in ('id','name','color','rank','grade','type','level','description','required_by','dropped_by','droprate','notes','worth') if i.get(k) not in (None, [], '')}
    if st: d['stats'] = st
    if i.get('recipe'): d['recipe'] = [list(x.items()) for x in i['recipe']]
    if i['name'] + '.jpg' in icons: d['icon'] = 1
    out_items.append(d)
sk = {}
for s in skills:
    c = s.get('caster','')
    for cc in (c if isinstance(c, list) else [c]):
        sk.setdefault(cc, {})[s['name']] = {k: s[k] for k in ('type','cooldown','description','color') if s.get(k)}
out_b = []
for b in bosses:
    d = dict(b)
    d['skillinfo'] = {n: sk.get(b['name'], {}).get(n) for n in b.get('spells', []) if sk.get(b['name'], {}).get(n)}
    out_b.append(d)
data = {'items': out_items, 'bosses': out_b, 'heros': heros}
s = json.dumps(data, ensure_ascii=False, separators=(',',':'))
open(sys.argv[3] if len(sys.argv)>3 else 'data.js','w', encoding='utf-8').write('window.TW_DATA=' + s.replace('</', '<\\/') + ';')
print(len(s)//1024, 'KB', len(out_items), len(out_b), sum(len(b['skillinfo']) for b in out_b), 'skills matched of', len(skills))
