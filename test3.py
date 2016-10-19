import Image

from sets import Set

photo = Image.open('c:/moje/aaa/arrow2.gif')

photo = photo.convert('RGB')

width = photo.size[0]  # define W and H
height = photo.size[1]

s = Set()
for y in range(0, height):
    for x in range(0, width):
        RGB = photo.getpixel((x, y))
        R, G, B = RGB
        s.add((R, G, B))

        print RGB

print s

