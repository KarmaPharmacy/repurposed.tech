import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dist/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for openDonorModal definition and usage
idx = text.find('function openDonorModal')
print("=== openDonorModal function ===")
print(text[idx:idx+800])

idx2 = text.find('function renderDonors')
print("=== renderDonors function ===")
print(text[idx2:idx2+800])

idx3 = text.find('id="donorModal"')
print("=== id='donorModal' markup ===")
print(text[idx3:idx3+600])
