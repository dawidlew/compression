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
        for _, char in enumerate(line):
          # print("char: '%s'" % str(char))
          if last <> char:
            ll.append(sl)
            sl = {}
            sl[str(char)] = 1
          else:
            sl[str(char)] += 1
          # print(str(sl))
          last = char
        # print sl
    # print ll
    cleaning_set(ll)


def cleaning_set(ll):
    print ll[11]


# def write_file_content():



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
