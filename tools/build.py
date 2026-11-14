"""Собирает index.html из src/app.html + данных.
Использование (из корня репозитория):
  git clone --depth 1 https://github.com/sfarmani/twrpg-info.git ../twrpg-info
  git clone --depth 1 https://github.com/sfarmani/twicons.git ../twicons
  python3 tools/build.py ../twrpg-info ../twicons
"""
import os, subprocess, sys
info, icons = sys.argv[1], sys.argv[2]
os.makedirs('build', exist_ok=True)
names = '\n'.join(f for f in os.listdir(icons) if f.endswith('.jpg'))
open('build/icons.txt', 'w').write(names)
here = os.path.dirname(os.path.abspath(__file__))
subprocess.run([sys.executable, f'{here}/prep.py', info, 'build/icons.txt', 'build/data.js'], check=True)
subprocess.run([sys.executable, f'{here}/icons.py', icons, 'build/data.js', 'build/icons.js'], check=True)
app = open('src/app.html', encoding='utf-8').read()
data = open('build/data.js', encoding='utf-8').read(); ic = open('build/icons.js', encoding='utf-8').read()
open('index.html', 'w', encoding='utf-8').write(app.replace('<script>/*DATA*/</script>', '<script>' + data + '</script>\n<script>' + ic + '</script>'))
print('index.html готов')
