def print_world():
    for row in world:
        for char in row:
            print(char, end='')
        print(char)


def inner_location(row, col):
    return 1 < row < len(world) - 2 and \
           1 < col < len(world[0]) - 2


def locate_teleports():
    teleport_name_to_pos = {}
    teleport_pos_to_name = {}

    # iterate over entry tile
    for tile1_row in range(len(world)):
        for tile1_col in range(len(world[tile1_row])):
            tile1 = world[tile1_row][tile1_col]
            # must be capital letter
            if tile1.isupper():
                # check for second letter below or to the right
                for dr, dc in ((0, 1), (1, 0)):
                    tile2_row = tile1_row + dr
                    tile2_col = tile1_col + dc
                    # skip if out of world
                    if tile2_row >= len(world) or tile2_col >= len(world[tile2_row]):
                        continue
                    tile2 = world[tile2_row][tile2_col]
                    # must be capital letter
                    if tile2.isupper():
                        teleport_name = tile1 + tile2
                        if teleport_name not in teleport_name_to_pos:
                            teleport_name_to_pos[teleport_name] = []
                        found = False
                        # identify walkable space (.) around
                        for dr2, dc2 in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                            # first check for first tile
                            free_row = tile1_row + dr2
                            free_col = tile1_col + dc2
                            if free_row >= len(world) or free_col >= len(world[free_row]):
                                continue
                            if world[free_row][free_col] == '.':
                                teleport_name_to_pos[teleport_name].append({
                                    'enter': (tile1_row, tile1_col),
                                    'leave': (free_row, free_col),
                                    'inner': inner_location(tile1_row, tile1_col)
                                })
                                teleport_pos_to_name[(tile1_row, tile1_col)] = teleport_name
                                found = True

                            # if not found, check for second tile
                            if not found:
                                free_row = tile2_row + dr2
                                free_col = tile2_col + dc2
                                if free_row >= len(world) or free_col >= len(world[free_row]):
                                    continue
                                if world[free_row][free_col] == '.':
                                    teleport_name_to_pos[teleport_name].append({
                                        'enter': (tile2_row, tile2_col),
                                        'leave': (free_row, free_col),
                                        'inner': inner_location(tile2_row, tile2_col)
                                    })
                                    teleport_pos_to_name[(tile2_row, tile2_col)] = teleport_name

    return teleport_name_to_pos, teleport_pos_to_name


def find_neighbors(teleport_name, teleport_name_to_pos, teleport_pos_to_name):
    result = {
        'inner': [],  # neighbors when teleport_name is inner
        'outer': []   # neighbors when teleport_name is outer
    }
    teleport_positions = teleport_name_to_pos[teleport_name]
    
    # add all teleport positions to to_visit
    to_visit = []
    for teleport_pos in teleport_positions:
        teleport_row, teleport_col = teleport_pos['leave']
        inner = teleport_pos['inner']

        to_visit.append((teleport_row, teleport_col, 0))

        visited = set()
        while to_visit:
            row, col, distance = to_visit.pop(0)

            # if neighbor found
            if (row, col) in teleport_pos_to_name and teleport_name != teleport_pos_to_name[row, col]:
                result['inner' if inner else 'outer'].append({
                    'distance': distance,
                    'name': teleport_pos_to_name[(row, col)],
                    'inner': inner_location(row, col)
                })
                continue

            # if visited or not empty space
            if (row, col) in visited or world[row][col] != '.':
                continue

            visited.add((row, col))

            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                to_visit.append((row + dr, col + dc, distance + 1))

    return result

# preparation - reading an input, locating teleports and paths
world = list(map(list, open('20.txt').read().split('\n')))
if world[-1] == []:
    world = world[:-1]

teleport_name_to_pos, teleport_pos_to_name = locate_teleports()
neighbors = {}
for teleport_name in teleport_name_to_pos.keys():
    neighbors[teleport_name] = find_neighbors(teleport_name, teleport_name_to_pos, teleport_pos_to_name)

# path search
to_visit = [("AA", False, 0, 0)]
visited = set()
found = False
while to_visit and not found:
    teleport_name, inner, distance, level = to_visit.pop(0)

    if level < 0:
        continue

    if (teleport_name, level, inner) in visited:
        continue

    visited.add((teleport_name, level, inner))

    current_neighbors = neighbors[teleport_name]['inner'] if inner else neighbors[teleport_name]['outer']
    for neighbor in current_neighbors:
        name = neighbor['name']
        new_distance = distance + neighbor['distance']
        next_level = level + 1 if neighbor['inner'] else level - 1

        if name == 'ZZ' and level == 0:
            print(new_distance - 1)
            found = True
            break

        to_visit.append((name, not neighbor['inner'], new_distance, next_level))
