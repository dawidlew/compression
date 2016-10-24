# coding=utf-8
import argparse
import os
from PIL import Image
import string

file = 'out.txt'

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


def write_file(path):
    u = compression_std(path)
    # print u

    x = []
    for item in u:
        for key, value in item.iteritems():
            x.append(key + str(value))
    print x

    print 'Zysk z kompresji (standard): %.02f%%' % (100 - ((size(os.getcwd() + '/' + file) * 1.0 / size(path)) * 100.0))
    my_file = open(file, "w")
    my_file.write("".join(x))

    write_bin(x)


def write_bin(x):
    import pickle

    output_file = open("out.bin", "wb")
    pickle.dump(x, output_file)
    output_file.close()


def compression_std(path):
    content = read_file_content(path)
    # print content
    pixels = get_colors(path)
    # print pixels

    n = []
    for i in content:
        for k, v in pixels.items():
            if i == v:
                n.append(k)
    # print n

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
        args.filepath = 'c:/moje/aaa/arrow2.gif'

    write_file(args.filepath)
