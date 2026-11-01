import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dist/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function renderDonors')
end = text.find('function openDonorModal')
print(text[idx:end])
