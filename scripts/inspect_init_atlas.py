import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dist/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function initAtlas')
print(text[idx:idx+800])
