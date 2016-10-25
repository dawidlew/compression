# coding=utf-8
import argparse
import os
from PIL import Image
import string
import pickle

file = 'out.txt'


def write_file(path):
    content = read_file_content(path)
    pixels = get_colors(path)
    u = compression_std(content, pixels)
    x = dict_to_list(u)
    im = Image.open(path)

    print 'Zysk z kompresji (standard): %.02f%%' % (100 - ((size(os.getcwd() + '/' + file) * 1.0 / size(path)) * 100.0))
    my_file = open(file, "w")
    my_file.write(str(im.size) + "".join(x))

    print ("".join(x))
    write_bin(x)


def size(path):
    return os.path.getsize(path)


def read_file_content(path):
    photo = Image.open(path)
    photo = photo.convert('RGB')
    width = photo.size[0]  # define W and H
    height = photo.size[1]

    s = []
    for y in range(0, height):
        for x in range(0, width):
            RGB = photo.getpixel((x, y))
            R, G, B = RGB
            s.append((R, G, B))
    return s



# przejście ze słownika na listę
def dict_to_list(u):

    x = []
    for item in u:
        for key, value in item.iteritems():
            x.append(key + str(value))
    return x


def write_bin(x):
    output_file = open("out.bin", "wb")
    pickle.dump(x, output_file)
    output_file.close()


def compression_std(content, pixels):

    n = []
    for i in content:
        for k, v in pixels.items():
            if i == v:
                n.append(k)
    ll = []
    sl = {}
    last = None
    for i, char in enumerate(n):
      if last <> char:
        sl = {}
        ll.append(sl)
        sl[(char)] = 1
      else:
        sl[(char)] += 1
      last = char
    return ll


def get_colors(path):

    img = Image.open(path)
    colors = img.convert('RGB').getcolors()

    pixel = []
    for item in colors:
        pixel.append((item[1]))
    z = dict(zip(string.letters, pixel))
    return z


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--filepath", type=str,
                        help="Path to the file",
                        required=False)
    args = parser.parse_args()

    # if not args.filepath:
    #     args.filepath = raw_input('Please input path and name of the file > ')

    if not args.filepath:
        args.filepath = 'c:/moje/aaa/Staszek i miecz.gif'

    write_file(args.filepath)
