import sys

from PIL import Image

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
