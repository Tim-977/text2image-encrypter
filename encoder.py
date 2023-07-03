import sys
from math import ceil, sqrt

from PIL import Image

# !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ 

if sys.platform == 'win32':
    import msvcrt

    def get_key():
        return msvcrt.getch()

else:
    import termios
    import tty

    def get_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def close():
    print("\nPress any key to exit...")
    while True:
        if get_key():
            break


characters = [chr(i) for i in range(33, 127)]
characters.append(' ')

dct = dict()

for elem in characters:
    dct[elem] = '0' * 4 + hex(ord(elem))[2:]

print('Avaliable charset: !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ')

word = input('Enter text:\n')

try:
    colors = [dct[elem] for elem in word]
except KeyError as exception:
    print('Unexpected character', exception)
    close()

width = height = ceil(sqrt(len(word)))

print(f"\n{len(word)} / {width * height} | .{round(len(word) / (width * height) * 100)}")

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

close()
