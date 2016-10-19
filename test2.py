from PIL import Image
im = Image.open('c:/moje/aaa/mouse_min.png')

pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

print pixels

