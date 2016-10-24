
from PIL import Image
import string

img = Image.open('c:/moje/aaa/arrow2.gif')
colors = img.convert('RGB').getcolors()


pixel = []
for item in colors:
    pixel.append((item[1]))

z = dict(zip(string.letters, pixel))

print pixel


# for a in string.letters:
#     print 3*a


