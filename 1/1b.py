data = open('1.txt').read().split()

s = 0
for n in data:
    n = int(n)
    while True:
        n = n // 3 - 2
        if n < 0:
            break
        s += n

print(s)
