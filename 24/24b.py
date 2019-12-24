def print_bugs(bugs):
    levels = bugs.keys()
    for level in range(min(levels), max(levels)+1):
        print(f'Depth {level}')
        for row in bugs[level]:
            for tile in row:
                print(tile, end='')
            print()
        print()


def print_counts(counts):
    levels = counts.keys()
    for level in range(min(levels), max(levels)+1):
        print(f'Depth {level}')
        for row in range(5):
            for col in range(5):
                print(counts[level][(row, col)], end='')
            print()
        print()


def count_around(bugs):
    result = {}
    levels = bugs.keys()
    for level in range(min(levels), max(levels)+1):
        result[level] = {}
        for r in range(5):
            for c in range(5):
                total = 0

                # if outer corner
                if (r, c) in [(0, 0), (0, 4), (4, 0), (4, 4)]:
                    # from same level
                    if r == 0:
                        total += 1 if bugs[level][1][c] == '#' else 0
                    if c == 0:
                        total += 1 if bugs[level][r][1] == '#' else 0
                    if r == 4:
                        total += 1 if bugs[level][3][c] == '#' else 0
                    if c == 4:
                        total += 1 if bugs[level][r][3] == '#' else 0

                    # from outer level
                    if level-1 in bugs:
                        if r == 0:
                            total += 1 if bugs[level-1][1][2] == '#' else 0
                        if c == 0:
                            total += 1 if bugs[level-1][2][1] == '#' else 0
                        if r == 4:
                            total += 1 if bugs[level-1][3][2] == '#' else 0
                        if c == 4:
                            total += 1 if bugs[level-1][2][3] == '#' else 0

                # if outer wall
                elif r == 0 or c == 0 or r == 4 or c == 4:
                    # from same level
                    if r == 0:
                        total += 1 if bugs[level][r][c-1] == '#' else 0
                        total += 1 if bugs[level][r][c+1] == '#' else 0
                        total += 1 if bugs[level][r+1][c] == '#' else 0
                    if c == 0:
                        total += 1 if bugs[level][r-1][c] == '#' else 0
                        total += 1 if bugs[level][r][c+1] == '#' else 0
                        total += 1 if bugs[level][r+1][c] == '#' else 0
                    if r == 4:
                        total += 1 if bugs[level][r][c-1] == '#' else 0
                        total += 1 if bugs[level][r][c+1] == '#' else 0
                        total += 1 if bugs[level][r-1][c] == '#' else 0
                    if c == 4:
                        total += 1 if bugs[level][r-1][c] == '#' else 0
                        total += 1 if bugs[level][r][c-1] == '#' else 0
                        total += 1 if bugs[level][r+1][c] == '#' else 0

                    # from outer level
                    if level-1 in bugs:
                        if r == 0:
                            total += 1 if bugs[level-1][1][2] == '#' else 0
                        if c == 0:
                            total += 1 if bugs[level-1][2][1] == '#' else 0
                        if r == 4:
                            total += 1 if bugs[level-1][3][2] == '#' else 0
                        if c == 4:
                            total += 1 if bugs[level-1][2][3] == '#' else 0

                # if inner corner
                elif (r, c) in [(1, 1), (1, 3), (3, 1), (3, 3)]:
                    # only same level
                    if (r, c) == (1, 1):
                        total += 1 if bugs[level][0][1] == '#' else 0
                        total += 1 if bugs[level][1][0] == '#' else 0
                        total += 1 if bugs[level][1][2] == '#' else 0
                        total += 1 if bugs[level][2][1] == '#' else 0
                    if (r, c) == (1, 3):
                        total += 1 if bugs[level][0][3] == '#' else 0
                        total += 1 if bugs[level][1][2] == '#' else 0
                        total += 1 if bugs[level][1][4] == '#' else 0
                        total += 1 if bugs[level][2][3] == '#' else 0
                    if (r, c) == (3, 1):
                        total += 1 if bugs[level][2][1] == '#' else 0
                        total += 1 if bugs[level][3][0] == '#' else 0
                        total += 1 if bugs[level][3][2] == '#' else 0
                        total += 1 if bugs[level][4][1] == '#' else 0
                    if (r, c) == (3, 3):
                        total += 1 if bugs[level][2][3] == '#' else 0
                        total += 1 if bugs[level][3][2] == '#' else 0
                        total += 1 if bugs[level][3][4] == '#' else 0
                        total += 1 if bugs[level][4][3] == '#' else 0

                # if inner wall
                elif r == 1 or c == 1 or r == 3 or c == 3:
                    # from same level
                    if r == 1:
                        total += 1 if bugs[level][0][2] == '#' else 0
                        total += 1 if bugs[level][1][1] == '#' else 0
                        total += 1 if bugs[level][1][3] == '#' else 0
                    if c == 1:
                        total += 1 if bugs[level][2][0] == '#' else 0
                        total += 1 if bugs[level][1][1] == '#' else 0
                        total += 1 if bugs[level][3][1] == '#' else 0
                    if r == 3:
                        total += 1 if bugs[level][4][2] == '#' else 0
                        total += 1 if bugs[level][3][1] == '#' else 0
                        total += 1 if bugs[level][3][3] == '#' else 0
                    if c == 3:
                        total += 1 if bugs[level][2][4] == '#' else 0
                        total += 1 if bugs[level][1][3] == '#' else 0
                        total += 1 if bugs[level][3][3] == '#' else 0

                    # from outer level
                    if level+1 in bugs:
                        if r == 1:
                            for t in range(5):
                                total += 1 if bugs[level+1][0][t] == '#' else 0
                        if c == 1:
                            for t in range(5):
                                total += 1 if bugs[level+1][t][0] == '#' else 0
                        if r == 3:
                            for t in range(5):
                                total += 1 if bugs[level+1][4][t] == '#' else 0
                        if c == 3:
                            for t in range(5):
                                total += 1 if bugs[level+1][t][4] == '#' else 0

                result[level][(r, c)] = total

    return result


def minute(bugs, counts):
    new_bugs = {}

    levels = bugs.keys()
    min_level = min(levels)
    max_level = max(levels)

    for level in levels:
        new_bugs[level] = empty_level()
        added = False
        for r in range(5):
            for c in range(5):
                num = counts[level][(r, c)]
                new_bugs[level][r][c] = bugs[level][r][c]
                if bugs[level][r][c] == '#' and num != 1:
                    new_bugs[level][r][c] = '.'
                elif bugs[level][r][c] == '.' and num in (1, 2):
                    new_bugs[level][r][c] = '#'
                    added = True

        if level == min_level and added:
            new_bugs[level - 1] = empty_level()

        if level == max_level and added:
            new_bugs[level + 1] = empty_level()

    return new_bugs


def empty_level(width=5, height=5):
    return [['.' for _ in range(width)] for _ in range(height)]


def count_all_bugs(bugs):
    result = 0
    for level in bugs.keys():
        for r in range(5):
            for c in range(5):
                result += 1 if bugs[level][r][c] == '#' else 0

    return result


bug_level_0 = list(map(list, open('24.txt').read().split('\n')[:-1]))

bugs = {
    0: bug_level_0,
    1: empty_level(),
    -1: empty_level()
}


for step in range(200):
    counts = count_around(bugs)
    bugs = minute(bugs, counts)

print(count_all_bugs(bugs))
