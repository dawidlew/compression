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


def stat(path):
    with open(path, 'r') as fp:
        col_len = max((nr[0]) for nr in enumerate(fp))
        print 'col_len: ' + str(col_len)
    with open(path, 'r') as fp:
        row_len = max(len(line) for nr, line in enumerate(fp))
        print 'row_len: ' + str(row_len)

    # compression(col_len, row_len, path)


def compression(path):
    with open(path, 'r') as fp:
        for rows, item in enumerate(fp):
            results = {}
            for c in item:

                col = collections.Counter(c)
                # # print col
                results[ord(c)] = col[c]
                # results[ord(c)] = c + 1
            print results




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
