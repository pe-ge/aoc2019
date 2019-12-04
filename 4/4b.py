min_val=[1, 7, 2, 9, 3, 0]
max_val=[6, 8, 3, 0, 8, 2]

def two_digits_and_no_group(val):
    return (val[0] == val[1] and val[1] != val[2]) or \
           (val[0] != val[1] and val[1] == val[2] and val[2] != val[3]) or \
           (val[1] != val[2] and val[2] == val[3] and val[3] != val[4]) or \
           (val[2] != val[3] and val[3] == val[4] and val[4] != val[5]) or \
           (val[3] != val[4] and val[4] == val[5])

def increase(val):
    val[5] += 1
    for idx in range(5, 0, -1):
        if val[idx] == 10:
            val[idx] = 0
            val[idx-1] += 1
        else:
            break
    return val

def make_ascending(val):
    for i in range(1, 6):
        if val[i-1] > val[i]:
            for j in range(i, 6):
                val[j] = val[i-1]
            break
    return val

total = 1
val = make_ascending(min_val[:])

while val < max_val:
    val = increase(val)
    val = make_ascending(val)

    if two_digits_and_no_group(val):
        print(val)
        total += 1

print(total - 1)
