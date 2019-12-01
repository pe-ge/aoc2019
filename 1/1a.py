from math import floor
print(sum(map(lambda n: floor(int(n)/3) - 2, open('1.txt').read().split())))
