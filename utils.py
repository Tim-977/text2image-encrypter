from math import ceil, sqrt

from PIL import Image

# !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ 

def encode(word):

    characters = [chr(i) for i in range(33, 127)]
    characters.append(' ')

    dct = dict()

    for elem in characters:
        dct[elem] = '0' * 4 + hex(ord(elem))[2:]

    try:
        colors = [dct[elem] for elem in word]
    except KeyError as exception:
        return ('Unexpected character', exception)

    width = height = ceil(sqrt(len(word)))

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

    new_image.save("static\\output.png")

    return 'image saved successfully'


def decode():

    characters = [chr(i) for i in range(33, 127)]
    characters.append(' ')

    dct = dict()

    for elem in characters:
        dct['0' * 4 + hex(ord(elem))[2:]] = elem

    image_path = "static\\output.png"
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

    return encoded_text
