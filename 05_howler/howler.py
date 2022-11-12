#!/usr/bin/env python3
"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2022-11-11
Purpose: Howler
"""

import argparse
from sys import stdout
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    text = args.text
    if os.path.isfile(text):
        with open(text, "r", encoding='utf-8') as file:
            text = file.read().rstrip()

    target = open(args.outfile, 'wt', encoding='utf-8') \
        if args.outfile else stdout
    target.write(f"{text.upper()}\n")
    target.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
