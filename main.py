import sys
from math import ceil, sqrt

from PIL import Image

# !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ 

def encode():
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

def decode():
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
        dct['0' * 4 + hex(ord(elem))[2:]] = elem

    image_path = "output.png"
    encoded_text = ""

    image = Image.open(image_path)
    width, height = image.size

    pixels = image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            hex_color = f"#{r:02x}{g:02x}{b:02x}"[
                1:][:3] + f"#{r:02x}{g:02x}{b:02x}"[1:][
                    4] + f"#{r:02x}{g:02x}{b:02x}"[1:][
                        3] + f"#{r:02x}{g:02x}{b:02x}"[1:][5:]

            if hex_color in dct:
                encoded_text += dct[hex_color]

    print(encoded_text)

    close()

flag = True

while flag:
    print('Do you want to encode or decode? Enter (e/d)')
    choice = input()

    if choice == 'e':
        encode()
        flag = False
    elif choice == 'd':
        decode()
        flag = False
    else:
        print('Unexpected answer, try again. (Type \'e\' or \'d\')\n')
