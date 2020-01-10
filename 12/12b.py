import numpy as np
from collections import defaultdict
from math import gcd

def extract_pos(pos):
    result = []
    pos = pos[1:-1]
    pos = pos.replace(',', '')
    for value in pos.split(' '):
        result.append(int(value[value.index('=')+1:]))
    return result

positions = list(map(extract_pos, open('12.txt').read().split('\n')))
init_positions = np.copy(positions)
velocities = np.zeros_like(positions)

histories = defaultdict(list)
step = 0
while True:
    # update velocities
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            for dim in range(3):
                if positions[i][dim] < positions[j][dim]:
                    diff = [1, -1]
                elif positions[i][dim] > positions[j][dim]:
                    diff = [-1, 1]
                else:
                    diff = [0, 0]
                velocities[i][dim] += diff[0]
                velocities[j][dim] += diff[1]

    # update positions
    positions += velocities
    step += 1

    # accumulate histories
    for idx in range(len(positions)):
        for dim in range(3):
            if positions[idx][dim] == init_positions[idx][dim] and velocities[idx][dim] == 0:
                histories[(idx, dim)].append(step)

    # stop after some time
    if step > 1000000:
        break

def find_cycle(history):
    cycle_len = 0
    while True:
        cycle_len += 1
        cycle = history[:cycle_len]
        for cycle_start in range(0, len(history), cycle_len):
            next_cycle = history[cycle_start:cycle_start+cycle_len]
            if len(next_cycle) != cycle_len:
                continue
            if cycle != next_cycle:
                break
        else:
            return sum(history[:cycle_len])

# find cycles for each (idx, dim)
cycles = []
for key, history in histories.items():
    diffs = []
    for idx in range(1, len(history)):
        diffs.append(history[idx] - history[idx-1])
    cycles.append(find_cycle(diffs))

# compute least common multiple
lcm = cycles[0]
for i in cycles[1:]:
    lcm = int(lcm*i/gcd(lcm, i))
print(lcm)
