from math import inf


def update_world_and_find_items(world):
    found = False
    start_r, start_c = None, None
    keys = {}
    for row_idx in range(len(world)):
        for col_idx in range(len(world[row_idx])):
            tile = world[row_idx][col_idx]
            if not found and tile == '@':
                start_r = row_idx
                start_c = col_idx
                for diff in range(-1, 2):
                    world[row_idx][col_idx + diff] = '#'
                    world[row_idx + diff][col_idx] = '#'

                world[row_idx - 1][col_idx - 1] = '@'
                world[row_idx + 1][col_idx - 1] = '@'
                world[row_idx - 1][col_idx + 1] = '@'
                world[row_idx + 1][col_idx + 1] = '@'

                found = True

            if tile.islower():
                keys[tile] = (row_idx, col_idx)

    return keys, (start_r, start_c)


def search_reachable(item_r, item_c):
    to_visit = [(item_r, item_c, 0, set())]

    visited = set()
    result = {}
    while to_visit:
        r, c, distance, required_doors = to_visit.pop(0)

        if (r, c) in visited or world[r][c] == '#':
            continue

        new_door = set([world[r][c]] if world[r][c].isupper() else [])

        visited.add((r, c))

        if world[r][c].islower() and (r != item_r or c != item_c):
            result[world[r][c]] = {
                'd': distance,
                'required': required_doors
            }

        next_required_doors = required_doors.union(new_door)
        to_visit.append((r+1, c, distance+1, next_required_doors))
        to_visit.append((r-1, c, distance+1, next_required_doors))
        to_visit.append((r, c+1, distance+1, next_required_doors))
        to_visit.append((r, c-1, distance+1, next_required_doors))

    return result


def backtrack(paths, robots, num_all_keys, num_found_keys, distance, visited):
    if num_found_keys == num_all_keys:
        global lowest_distance
        if distance < lowest_distance:
            lowest_distance = distance
            print(distance)
        return

    for robot_idx, robot in enumerate(robots):
        for key, params in paths[robot].items():
            if key in visited:
                continue

            have_required_keys = True
            for required_door in params['required']:
                if required_door.lower() not in visited:
                    have_required_keys = False
                    break

            if not have_required_keys:
                continue

            visited.add(key)
            tmp = robots[robot_idx]
            robots[robot_idx] = key
            backtrack(paths, robots, num_all_keys, num_found_keys+1, distance + params['d'], visited)
            robots[robot_idx] = tmp
            visited.remove(key)


world = list(map(list, open('18.txt').read().split('\n')))
keys, (start_r, start_c) = update_world_and_find_items(world)

paths = {
    'TL': search_reachable(start_r - 1, start_c - 1),
    'TR': search_reachable(start_r - 1, start_c + 1),
    'BL': search_reachable(start_r + 1, start_c - 1),
    'BR': search_reachable(start_r + 1, start_c + 1)
}

for key, (r, c) in keys.items():
    paths[key] = search_reachable(r, c)

robots = ['TL', 'TR', 'BL', 'BR']
lowest_distance = inf
backtrack(paths, robots, len(keys), 0, 0, set())
print(lowest_distance)
