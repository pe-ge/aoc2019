import numpy as np

def extract_pos(pos):
    result = []
    pos = pos[1:-1]
    pos = pos.replace(',', '')
    for value in pos.split(' '):
        result.append(int(value[value.index('=')+1:]))
    return result

positions = list(map(extract_pos, open('12.txt').read().split('\n')))
velocities = np.zeros_like(positions)

steps = 1000
for _ in range(steps):
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

    # calc energy
    potential_energy = np.sum(np.abs(positions), axis=1)
    kinetic_energy = np.sum(np.abs(velocities), axis=1)
    energy = np.sum(np.multiply(potential_energy, kinetic_energy))

print(energy)
