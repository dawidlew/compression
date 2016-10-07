# coding=utf-8
import argparse
import collections
import string
import os
import sys
import mimetypes
import math
import re


def size(path):
    return os.path.getsize(path)


def read_file_content(path):
    file_h = open(path, 'r')
    content = file_h.readlines()
    file_h.close()
    return content

def write_file(path):
    s = compression1(path)
    # my_file = open("out.txt", "w")
    # my_file.write("Hello world")
    print s
    print 'Zysk z kompresji @: %.02f%%' % (100 - ((len(s) * 1.0 / size(path)) * 100.0))

    s = compression2(path)
    print s
    print 'Zysk z kompresji #: %.02f%%' % (100 - ((len(s) * 1.0 / size(path)) * 100.0))


def compression1(path):
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



def compression2(path):
    content = read_file_content(path)
    ll = []
    for line in reversed(content): # reversed odwraca linie
        sl = {}
        last = None
        line = line.strip()
        line = line[::-1]  # odwraca znaki w linii
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
        args.filepath = 'c:/moje/aaa/git_nauka/compression/test1.txt'

    write_file(args.filepath)
