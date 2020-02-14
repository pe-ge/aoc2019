m = 119315717514047
k = 101741582076661
x = 2020

def deal_into_new_stack():
    return -1, -1

def cut(n):
    return 1, -n

def increment(n):
    return n, 0

def compose(a, b, c, d):
    return (a * c) % m, (b * c + d) % m

def modinv(num):
    return pow(num, m-2, m)

shuffles = open('22.txt').read().split('\n')[:-1]

# compose shuffle into LCF
a, b = 1, 0
for shuffle in shuffles:
    if shuffle == 'deal into new stack':
        c, d = deal_into_new_stack()
    else:
        N = int(shuffle.split(' ')[-1])
        if 'deal' in shuffle:
            c, d = increment(N)
        else:
            c, d = cut(N)

    a, b = compose(a, b, c, d)


A = pow(a, k, m)
Ainv = modinv(A)
B = (b * modinv(1 - a)) % m

print(((x - B) * Ainv + B) % m)

# sources
# https://codeforces.com/blog/entry/72527
# https://codeforces.com/blog/entry/72593
