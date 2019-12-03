from math import inf
wires = open('3.txt').read().split()

directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1)
}

paths = []
paths_set = []
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
    paths.append(path)
    paths_set.append(set(path))

crosses = paths_set[0] & paths_set[1]
crosses.remove((0, 0))

crosses_dict = {}
for cross in crosses:
    crosses_dict[cross] = 0

for path in paths:
    for point_idx, point in enumerate(path):
        if point in crosses:
            crosses_dict[point] += point_idx

min_steps = inf
for steps in crosses_dict.values():
    min_steps = min(min_steps, steps)
print(min_steps)
