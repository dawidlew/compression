import Image

photo = Image.open('c:/moje/aaa/arrow2.gif')

photo = photo.convert('RGB')

width = photo.size[0]  # define W and H
height = photo.size[1]

s = []
for y in range(0, height):
    for x in range(0, width):
        RGB = photo.getpixel((x, y))
        R, G, B = RGB
        s.append((R, G, B))

print s
