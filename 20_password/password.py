#!/usr/bin/env python3
"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2022-11-22
Purpose: Password maker
"""

import argparse
import sys
from typing import Final
import string
import random


LEET_CODE: Final = {
    'a': '@',
    'A': '4',
    'O': '0',
    't': '+',
    'E': '3',
    'I': '1',
    'S': '5'
}


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        default=[sys.stdin],
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--num',
                        help='Number of passwords to generate',
                        metavar='num_passwords',
                        type=int,
                        default=3)

    parser.add_argument('-w',
                        '--num_words',
                        help='Number of words to use for password',
                        metavar='num_words',
                        type=int,
                        default=4)

    parser.add_argument('-m',
                        '--min_word_len',
                        help='Minimum word length',
                        metavar='minimum',
                        type=int,
                        default=3)

    parser.add_argument('-x',
                        '--max_word_len',
                        help='Maximum word length',
                        metavar='maximum',
                        type=int,
                        default=6)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-l',
                        '--l33t',
                        help='Obfuscate letters',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    words = set()

    def word_len(word):
        return args.min_word_len <= len(word) <= args.max_word_len

    for file_handle in args.file:
        for line in file_handle:
            for word in filter(word_len, map(clean, line.lower().split())):
                words.add(word.title())

    words = sorted(words)
    passwords = [''.join(random.sample(words, args.num_words))
                 for _ in range(args.num)]

    if args.l33t:
        passwords = list(map(l33t, passwords))

    print('\n'.join(passwords))


# --------------------------------------------------
def clean(text: str):
    """Removes punctuation chars from string"""
    return ''.join(filter(lambda c: c not in string.punctuation, text))


def ransom(text: str):
    """Swaps char sensitiveness randomly"""
    return ''.join([c.upper() if random.choice([False, True]) else c.lower()
                    for c in text])


def l33t(text: str):
    """Encodes char in l33t style"""
    return ''.join([LEET_CODE.get(c, c) for c in ransom(text)])\
        + random.choice(string.punctuation)


# --------------------------------------------------
if __name__ == '__main__':
    main()
