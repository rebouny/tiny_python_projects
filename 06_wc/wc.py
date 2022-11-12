#!/usr/bin/env python3
"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2022-11-12
Purpose: word count
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='*',
                        default=[sys.stdin],
                        help='Input file(s)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    total_num_lines, total_num_words, total_num_bytes = 0, 0, 0

    for file_handle in args.file:
        num_lines, num_words, num_bytes = 0, 0, 0
        for line in file_handle:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)

        total_num_lines += num_lines
        total_num_words += num_words
        total_num_bytes += num_bytes

        print(f"{num_lines:8}{num_words:8}{num_bytes:8} {file_handle.name}")

    if len(args.file) > 1:
        print((f"{total_num_lines:8}{total_num_words:8}"
               f"{total_num_bytes:8} total"))


# --------------------------------------------------
if __name__ == '__main__':
    main()
