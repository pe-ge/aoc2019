def print_bugs(bugs):
    for row in bugs:
        for bug in row:
            print(bug, end='')
        print()
    print()


def count(bugs):
    result = {}
    for r in range(len(bugs)):
        for c in range(len(bugs[r])):
            total = 0
            for dr, dc in (1, 0), (-1, 0), (0, 1), (0, -1):
                rr = r + dr
                cc = c + dc
                if rr < 0 or cc < 0 or rr >= len(bugs) or cc >= len(bugs[rr]):
                    continue

                total += 1 if bugs[rr][cc] == '#' else 0
            result[(r, c)] = total

    return result


def minute(bugs, counts):
    new_bugs = []
    for r in range(len(bugs)):
        new_bugs.append([])
        for c in range(len(bugs[r])):
            num = counts[(r, c)]
            if bugs[r][c] == '#' and num != 1:
                new_bugs[-1].append('.')
            elif bugs[r][c] == '.' and num in (1, 2):
                new_bugs[-1].append('#')
            else:
                new_bugs[-1].append(bugs[r][c])

    return new_bugs


def hash(bugs):
    return ''.join([''.join(row) for row in bugs])


bugs = list(map(list, open('24.txt').read().split('\n')[:-1]))
history = set()
history.add(hash(bugs))

step = 0
while True:
    counts = count(bugs)
    bugs = minute(bugs, counts)
    hash_bugs = hash(bugs)
    if hash_bugs in history:
        break
    history.add(hash_bugs)
    step += 1

factor = 0
result = 0
for r in range(len(bugs)):
    for c in range(len(bugs[r])):
        if bugs[r][c] == '#':
            result += (2 ** factor)
        factor += 1

print(result)
