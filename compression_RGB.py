# coding=utf-8
import argparse
import os
import Image


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

    print 'Zysk z kompresji (standard): %.02f%%' % (100 - ((len(u) * 1.0 / size(path)) * 100.0))
    my_file = open("out.txt", "w")
    my_file.write(str(u) + '@')

    print 'u: ' + str(u)

    write_bin(u)

def write_bin(u):
    import pickle

    output_file = open("out.bin", "wb")
    pickle.dump(u, output_file)
    output_file.close()


def compression_std(path):
    content = read_file_content(path)
    print content

    ll = []
    sl = {}
    last = None
    for i, char in enumerate(content):
      if last <> char:
        sl = {}
        ll.append(sl)
        sl[(char)] = 1
      else:
        sl[(char)] += 1
      last = char

    return ll


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
