#!/usr/bin/env python3
"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2022-11-14
Purpose: Ransom Note

The original problem ignores cases sensitiveness of input text. By using
``str.swapcase()`` we can improve that, but our test won't work then.
Therefore input text gets converted to lowercase. Feel free to remove it.
"""

import argparse
import random
import os
import io
from typing import Final

CHAR_ENCODING: Final = {
    'A': '4',
    'B': '|3',
    'C': '(',
    'D': '|)',
    'E': '3',
    'F': '|=',
    'G': '(-',
    'H': '|-|',
    'I': '1',
    'J': '_|',
    'K': '|<',
    'L': '|_',
    'M': '|\\/|',
    'N': '|\\|',
    'P': '|`',
    'Q': '',
    'R': '',
    'S': '5',
    'T': '+',
    'V': '\\/',
    'W': '\\/\\/'
}


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

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
    random.seed(args.seed)
    for text in args.text:
        print("".join(map(choose, text.rstrip().lower())))


# --------------------------------------------------
def choose(char: str):
    """Swaps char sensitiveness randomly"""
    return char.swapcase() if random.choice([False, True]) else char


def test_choose():
    """Test for choosing"""
    state = random.getstate()
    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'C'
    assert choose('d') == 'd'
    random.setstate(state)


def encode_chars(char: str):
    """Leet encoder"""
    return CHAR_ENCODING.get(char.upper(), char) \
        if random.choice([False, True]) else char


def test_encode():
    """Test our leet encoder"""
    text = 'The quick brown fox jumps over the lazy dog.'
    state = random.getstate()
    random.seed(1)
    assert "".join(map(encode_chars, text.rstrip().lower())) \
        == 'th3 u1(k |3ro\\/\\/n |=ox jump5 ove t|-|e |_4zy dog.'
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
