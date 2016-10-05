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


def compression(path):
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

    cleaning_set(ll, path)


def cleaning_set(ll, path):
    s = ''
    for v in ll:
        for kk, vv in v.items():
            if vv == 1:
                vv = ""
            elif vv == 2:
                vv = str(kk)
            s += str(kk) + str(vv)
    print s
    print 'Zysk z kompresji: %.02f%%' % (100 - ((len(s) * 1.0 / size(path)) * 100.0))


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

    compression(args.filepath)
