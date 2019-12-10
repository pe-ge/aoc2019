from math import gcd

def calc_asteroids_at_angle(data, row, col, dr, dc):
    while True:
        if row+dr < 0 or col+dc < 0 or row+dr >= len(data) or col+dc >= len(data[0]):
            return 0
        if data[row+dr][col+dc] == '#':
            return 1

        row += dr
        col += dc

def calc_asteroids(data, row, col, angles):
    count = 0
    for (dr, dc) in angles:
        count += calc_asteroids_at_angle(data, row, col, dr, dc)

    return count

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

data = open('10.txt').read().split('\n')
angles = create_angles()
asteroids = {}
max_val = 0
max_pos = None
for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col] != '#':
            continue
        asteroids[(row, col)] = calc_asteroids(data, row, col, angles)
        if asteroids[(row, col)] > max_val:
            max_val = asteroids[(row, col)]
            max_pos = (row, col)

print(max_pos, max_val)

