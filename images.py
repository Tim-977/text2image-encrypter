from PIL import Image
from pprint import pprint
import sys

characters = [chr(i) for i in range(33, 127)]
characters.append(' ')

dct = dict()

for elem in characters:
    dct[elem] = '0' * 3 + hex(ord(elem))[2:] + 1 * '0'

word = 5 * 'Eelit non id lectus cras, nostra feugiat fusce leo eget libero nascetur tincidunt dignissim ad, auctor sollicitudin fringilla porttitor scelerisque conubia turpis porta dis pulvinar. Sapien congue metus lacinia sagittis cras porta nascetur habitasse tristique molestie elementum cubilia egestas porttitor, litora laoreet etiam neque dis ullamcorper fusce sem cursus morbi nisi odio ut. Luctus fermentum enim dui donec nullam vulputate suscipit, platea hendrerit primis dictumst mauris facilisis magnis, ac ex dis libero vel sed. Tellus nascetur nulla nunc varius rhoncus porttitor, ornare senectus egestas ac vitae fusce tortor, scelerisque auctor primis eros consectetur. Magnis nisi tempus finibus magna turpis aliquet nascetur nam mollis, habitant tellus nisl tristique varius rutrum semper gravida, nostra ipsum dictum facilisi suspendisse vestibulum penatibus per. Aptent erat nam molestie dictumst auctor morbi, tristique pretium lacinia dis gravida proin aenean, iaculis natoque elit varius ut. Lorem malesuada vehicula integer ullamcorper aliquam est molestie, diam nisi ultrices lobortis orci vel, iaculis enim quis laoreet elit quisque. Eleifend fermentum dictum pharetra nullam nunc iaculis sodales pellentesque aenean ex egestas, a nibh gravida felis fames laoreet vel euismod pretium. Quisque pulvinar nascetur lacus metus convallis mauris cras leo commodo mattis id maximus diam, integer finibus habitasse consectetur risus neque vitae magna molestie orci tortor maecenas, velit at placerat ac turpis conubia nullam imperdiet libero habitant ex eu. Luctus laoreet facilisi sociosqu dapibus praesent cursus etiam enim, ultricies pellentesque faucibus semper integer scelerisque ligula libero, tristique conubia dis tortor volutpat hendrerit egestas. Purus dignissim vestibulum orci aliquet ad quam sed cras nulla facilisis, euismod dapibus pretium congue nostra ultrices nullam posuere nec, penatibus blandit non viverra eleifend fermentum quis fames ornare.'

colors = [dct[elem] for elem in word]

width = 100
height = 100

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
