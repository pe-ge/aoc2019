from math import inf
imgs = list(map(int, open('8.txt').read()[:-1]))
w = 25
h = 6

start_idx = 0
min_zeros_idx = None
min_zeros = inf
while start_idx < len(imgs):
    img = imgs[start_idx:start_idx+w*h]
    num_zeros = img.count(0)

    if num_zeros < min_zeros:
        min_zeros = num_zeros
        min_zeros_idx = start_idx

    start_idx += w*h

img = imgs[min_zeros_idx:min_zeros_idx+w*h]
print(img.count(1) * img.count(2))
