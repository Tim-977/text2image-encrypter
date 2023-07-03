import sys
from math import ceil, sqrt

from PIL import Image

# !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ 

characters = [chr(i) for i in range(33, 127)]
characters.append(' ')

dct = dict()

for elem in characters:
    dct[elem] = '0' * 4 + hex(ord(elem))[2:]

print('Avaliable charset: !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ')

word = input('Enter text:\n')

colors = [dct[elem] for elem in word]

width = height = ceil(sqrt(len(word)))

print(f"{len(word)} / {width * height} | .{round(len(word) / (width * height) * 100)}")

new_image = Image.new("RGB", (width, height))

pixels = new_image.load()


for y in range(height):
    for x in range(width):
        try:
            hex_color = colors[y * width + x]
        except IndexError:
            hex_color = '000000'
        rgb_color = tuple(int(hex_color[i:i + 2], 16) for i in (1, 3, 5))
        pixels[x, y] = rgb_color

new_image.save("output.png")
