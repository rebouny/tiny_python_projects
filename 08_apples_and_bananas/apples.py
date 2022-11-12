#!/usr/bin/env python3
"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2022-11-12
Purpose: Find and replace
"""

import argparse
import os
import io


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        choices=list('aeiouAEIOU'),
                        default='a')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text, encoding='utf-8')
    else:
        args.text = io.StringIO(args.text + '\n')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    joined = "".join(args.vowel * 5) + "".join(args.vowel.upper() * 5)
    trans = str.maketrans('aeiouAEIOU', joined)

    for line in args.text:
        print(line.translate(trans))


# --------------------------------------------------
if __name__ == '__main__':
    main()
