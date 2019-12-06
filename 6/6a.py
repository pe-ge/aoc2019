data = open('6.txt').read().split()

orbits = {}
for orbit in data:
    aaa, bbb = orbit.split(')')
    orbits[bbb] = aaa

count = 0
for obj in orbits:
    count += 1
    while orbits[obj] in orbits:
        count += 1
        obj = orbits[obj]

print(count)
