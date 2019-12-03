from math import inf
wires = open('3.txt').read().split()

directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1)
}

paths = []
for wire in wires:
    turns = wire.split(',')
    path = [(0, 0)]
    for turn in turns:
        direction = turn[0]
        length = int(turn[1:])
        dx, dy = directions[direction]
        for _ in range(length):
            prev_x, prev_y = path[-1]
            path.append((prev_x + dx, prev_y + dy))
    paths.append(set(path))

crosses = paths[0] & paths[1]
crosses.remove((0, 0))
min_distance = inf
for cross in crosses:
    distance = abs(cross[0]) + abs(cross[1])
    min_distance = min(min_distance, distance)

print(min_distance)
