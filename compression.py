# coding=utf-8
import argparse
import os
import sys


def size(path):
    return os.path.getsize(path)


def read_file_content(path):
    file_h = open(path, 'r')
    content = file_h.readlines()
    file_h.close()
    return content

def write_file(path):
    s = compression_std(path)
    u = compression_90(path)

    # t = compression_odwrotnie(path)
    # print t
    # print 'Zysk z kompresji #: %.02f%%' % (100 - ((len(t) * 1.0 / size(path)) * 100.0))

    if u >= s:
        print 'Zysk z kompresji (standard): %.02f%%' % (100 - ((len(u) * 1.0 / size(path)) * 100.0))
        my_file = open("out.txt", "w")
        my_file.write(u + '@')

        print 'u: ' + u

    else:
        print 'Zysk z kompresji (90 stopni): %.02f%%' % (100 - ((len(s) * 1.0 / size(path)) * 100.0))
        my_file = open("out.txt", "w")
        my_file.write(s + '#')

        print 's: ' + s


def compression_90(path):
    content = read_file_content(path)

    result = [[content[j][i] for j in range(len(content))] for i in range(len(content[0]))]

    ll = []
    for line in result:
        sl = {}
        last = None
        for i, char in enumerate(line):
            if last <> char:
                sl = {}
                ll.append(sl)
                sl[(char)] = 1
            else:
                sl[(char)] += 1
            last = char
    u = cleaning_set(ll)
    return u


def compression_std(path):
    content = read_file_content(path)
    ll = []
    for line in content:
        sl = {}
        last = None
        line = line.strip()
        for i, char in enumerate(line):
          if last <> char:
            sl = {}
            ll.append(sl)
            sl[(char)] = 1
          else:
            sl[(char)] += 1
          last = char
    s = cleaning_set(ll)
    return s



# def compression_odwrotnie(path):
#     content = read_file_content(path)
#     ll = []
#     for line in reversed(content): # reversed odwraca linie
#         sl = {}
#         last = None
#         line = line.strip()
#         line = line[::-1]  # odwraca znaki w linii
#         for i, char in enumerate(line):
#           if last <> char:
#             sl = {}
#             ll.append(sl)
#             sl[(char)] = 1
#           else:
#             sl[(char)] += 1
#           last = char
#     s = cleaning_set(ll)
#     return s


def cleaning_set(set):
    s = ''
    for v in set:
        for kk, vv in v.items():
            if vv == 1:
                vv = ""
            elif vv == 2:
                vv = str(kk)
            s += str(kk) + str(vv)
    return s


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--filepath", type=str,
                        help="Path to the file",
                        required=False)
    args = parser.parse_args()

    # if not args.filepath:
    #     args.filepath = raw_input('Please input path and name of the file > ')

    if not args.filepath:
        args.filepath = 'c:/moje/aaa/git_nauka/compression/output_file.csv'

    write_file(args.filepath)
