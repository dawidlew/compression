# coding=utf-8
import argparse
import collections
import string
import os
import sys
import mimetypes
import math
import re


def read_file_content(path):
    file_h = open(path, 'r')
    content = file_h.read()
    file_h.close()

    # print content

    # size(path)
    # print os.path.getsize(path)

    stat(path)

def size(path):
    return os.path.getsize(path)


def stat(path):
    with open(path, 'r') as fp:

        for nr, line in enumerate(fp):
            print nr
            print line




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--filepath", type=str,
                        help="Path to the file",
                        required=True)
    args = parser.parse_args()

    path = args.filepath
    if path is None:
        path = raw_input('Please input path and name of the file > ')

    read_file_content(path)
