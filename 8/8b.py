imgs = list(map(int, open('8.txt').read()[:-1]))
w = 25
h = 6

num_imgs = len(imgs) // (w * h)

img = []
for num_pixel in range(w*h):
    for num_img in range(num_imgs):
        pixel = imgs[num_img * w*h + num_pixel]
        if pixel < 2:
            img.append(pixel)
            break

idx = 0
for r in range(h):
    for c in range(w):
        print(' ' if img[r*w + c] == 0 else '#', end='')
    print()
