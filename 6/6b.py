data = open('6.txt').read().split()

orbits = {}
for orbit in data:
    aaa, bbb = orbit.split(')')
    orbits[bbb] = aaa

your_path = []
obj = 'YOU'
while orbits[obj] in orbits:
    obj = orbits[obj]
    your_path.append(obj)

santa_path = []
obj = 'SAN'
while orbits[obj] in orbits:
    obj = orbits[obj]
    santa_path.append(obj)

for obj in your_path:
    if obj in santa_path:
        break

your_idx = your_path.index(obj)
santa_idx = santa_path.index(obj)
print(your_idx + santa_idx)
