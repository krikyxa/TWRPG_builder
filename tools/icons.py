import json, base64, io, os, sys
from PIL import Image
d = json.loads(open(sys.argv[2] if len(sys.argv)>2 else 'data.js', encoding='utf-8').read()[len('window.TW_DATA='):-1].replace('<\\/', '</'))
src = sys.argv[1]; out = {}
for it in d['items']:
    if not it.get('icon'): continue
    p = os.path.join(src, it['name'] + '.jpg')
    if not os.path.exists(p): continue
    im = Image.open(p).convert('RGB').resize((64, 64), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=82, optimize=True)
    out[it['name']] = 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
s = json.dumps(out, ensure_ascii=False, separators=(',', ':'))
open(sys.argv[3] if len(sys.argv)>3 else 'icons.js', 'w', encoding='utf-8').write('window.TW_ICONS=' + s.replace('</', '<\\/') + ';')
print(len(out), 'icons', len(s) // 1024, 'KB')
