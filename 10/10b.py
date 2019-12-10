from math import gcd
import math

def angle(v1, v2):
    dot = v1[0] * v2[0] + v1[1] * v2[1]
    det = v1[0] * v2[1] - v2[0] * v1[1]
    return math.atan2(det, dot)

def destroy(data, row, col, dr, dc, num):
    while True:
        if row+dr < 0 or col+dc < 0 or row+dr >= len(data) or col+dc >= len(data[0]):
            return None
        if data[row+dr][col+dc] == '#':
            data[row+dr][col+dc] = str(num)
            return (row+dr, col+dc)

        row += dr
        col += dc

def create_angles():
    angles = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for i in range(0, 40):
        for j in range(i+1,40):
            if gcd(i, j) == 1 or i == 1:
                angles.append((i, j))
                angles.append((i, -j))
                angles.append((-i, j))
                angles.append((-i, -j))

                angles.append((j, i))
                angles.append((j, -i))
                angles.append((-j, i))
                angles.append((-j, -i))
    return set(angles)

def print_map(data):
    for row in data:
        print(row)

data = list(map(list, open('10.txt').read().split('\n')))
best_row, best_col = (29, 26)  # from part A
angles = sorted(create_angles(), key=lambda x: angle((100000, 0), x), reverse=True)

idx = 0
count = 0
while True:
    val = destroy(data, 29, 26, angles[idx][0], angles[idx][1], count+1)
    if val is not None:
        count += 1
    idx = (idx + 1) % len(angles)
    if count == 200:
        break

print(val[1] * 100 + val[0])
