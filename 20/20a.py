from collections import defaultdict
world = list(map(list, open('20.txt').read().split('\n')))

def print_world():
    for row in world:
        for char in row:
            print(char, end='')
        print(char)

teleports = defaultdict(list)

# locate teleports
for row_idx in range(len(world)):
    for col_idx in range(len(world[row_idx])):
        tile = world[row_idx][col_idx]
        if tile.isupper():
            for dr, dc in ((0, 1), (1, 0)):
                row2_idx = row_idx + dr
                col2_idx = col_idx + dc
                # skip if second tile out of world
                if row2_idx >= len(world) or col2_idx >= len(world[row2_idx]):
                    continue
                tile2 = world[row2_idx][col2_idx]
                if tile2.isupper():
                    found = False
                    # identify walkable space (.) around
                    for dr2, dc2 in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        free_space_row_idx = row_idx + dr2
                        free_space_col_idx = col_idx + dc2
                        if free_space_row_idx >= len(world) or free_space_col_idx >= len(world[free_space_row_idx]):
                            continue
                        if world[free_space_row_idx][free_space_col_idx] == '.':
                            teleports[tile + tile2].append((row_idx, col_idx))
                            teleports[tile + tile2].append((free_space_row_idx, free_space_col_idx))
                            found = True

                        if not found:
                            free_space_row_idx = row2_idx + dr2
                            free_space_col_idx = col2_idx + dc2
                            if free_space_row_idx >= len(world) or free_space_col_idx >= len(world[free_space_row_idx]):
                                continue
                            if world[free_space_row_idx][free_space_col_idx] == '.':
                                teleports[tile + tile2].append((row2_idx, col2_idx))
                                teleports[tile + tile2].append((free_space_row_idx, free_space_col_idx))
                                found = True

start_r, start_c = teleports['AA'][1]
end_r, end_c = teleports['ZZ'][1]
jumps = {}
for teleport_name, teleport_locations in teleports.items():
    if len(teleport_locations) == 4:
        jumps[teleport_locations[0]] = teleport_locations[3]
        jumps[teleport_locations[2]] = teleport_locations[1]

to_visit = [(start_r, start_c, 0)]
visited = set()
while to_visit:
    row_idx, col_idx, d = to_visit.pop(0)
    # if end found
    if end_r == row_idx and end_c == col_idx:
        print(d)
        break

    if (row_idx, col_idx) in visited or world[row_idx][col_idx] != '.':
        continue

    visited.add((row_idx, col_idx))

    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        row2_idx = row_idx + dr
        col2_idx = col_idx + dc
        if (row2_idx, col2_idx) in jumps:
            to_visit.append(jumps[(row2_idx, col2_idx)] + (d+1,))
        else:
            to_visit.append((row2_idx, col2_idx, d+1))

