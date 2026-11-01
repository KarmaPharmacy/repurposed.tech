import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import scripts.encarta_data as d

print(f"Total existing donors: {len(d.DONORS_DATA)}")
cats = {}
for i, donor in enumerate(d.DONORS_DATA, 1):
    c = donor['cat']
    cats[c] = cats.get(c, 0) + 1
    print(f"{i:2d}. [{donor['cat']:10}] {donor['id']:30} : {donor['name']}")

print("\nDonor distribution by category:")
for c, count in cats.items():
    print(f"  {c:15}: {count}")
