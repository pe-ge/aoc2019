def find_start(world):
    num_keys = 0
    for row_idx in range(len(world)):
        for col_idx in range(len(world[row_idx])):
            if world[row_idx][col_idx] == '@':
                start_r = row_idx
                start_c = col_idx
            if world[row_idx][col_idx].islower():
                num_keys += 1
    return start_r, start_c, num_keys


world = list(map(list, open('18.txt').read().split('\n')))
start_r, start_c, num_all_keys = find_start(world)

to_visit = [(start_r, start_c, 0, 0, 0)]
visited = set()
while to_visit:
    r, c, keys, num_found_keys, distance = to_visit.pop(0)

    # ignore wall
    if world[r][c] == '#':
        continue

    # ignore visited
    if (r, c, keys) in visited:
        continue
    visited.add((r, c, keys))

    # if found door, check whether we have key
    if world[r][c].isupper():
        key = world[r][c].lower()
        key_binary = 2 ** (ord(key) - ord('a'))
        if keys & key_binary == 0:
            continue

    # if found key, append to variable keys
    new_keys = keys
    new_num_found_keys = num_found_keys
    if world[r][c].islower():
        key = world[r][c]
        key_binary = 2 ** (ord(key) - ord('a'))
        new_keys = keys | key_binary
        if new_keys != keys:
            new_num_found_keys = num_found_keys + 1

    # check if solution found
    if new_num_found_keys == num_all_keys:
        print(distance)
        break

    to_visit.append((r+1, c, new_keys, new_num_found_keys, distance + 1))
    to_visit.append((r-1, c, new_keys, new_num_found_keys, distance + 1))
    to_visit.append((r, c+1, new_keys, new_num_found_keys, distance + 1))
    to_visit.append((r, c-1, new_keys, new_num_found_keys, distance + 1))
