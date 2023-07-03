from PIL import Image
from pprint import pprint
import sys

characters = [chr(i) for i in range(33, 127)]
characters.append(' ')

dct = dict()

for elem in characters:
    dct[elem] = '0' * 4 + hex(ord(elem))[2:]

word = 'Hello everyone! How are u all guys doing?? I am doing very well btw, cya later ;))'

colors = [dct[elem] for elem in word]

width = 10
height = 10

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
