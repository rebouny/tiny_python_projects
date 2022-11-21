#!/usr/bin/env python3
"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2022-11-21
Purpose: Gematria
"""

import argparse
import os
import io
import string
from typing import Final
from functools import reduce


VALID_CHARS: Final = string.ascii_letters + string.digits


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input text or file')

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

    for text in args.text:
        print(' '.join([word2num(word) for word in text.split()]))


# --------------------------------------------------
def word2num(word):
    """Sums up ordinals of a word"""
    return str(reduce(lambda x, y: x + y, map(value, list(word))))


def value(char):
    """Maps valid char to ordinal value"""
    return ord(char) if char in VALID_CHARS else 0


def test_value():
    """Test value"""
    assert value("a") == 97
    assert value("Z") == 90
    assert value("'") == 0


def test_word2num():
    """Test word2num"""
    assert word2num("a") == "97"
    assert word2num("abc") == "294"
    assert word2num("ab'c") == "294"
    assert word2num("4a-b'c,") == "346"


# --------------------------------------------------
if __name__ == '__main__':
    main()
