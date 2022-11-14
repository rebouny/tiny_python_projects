#!/usr/bin/env python3
"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2022-11-14
Purpose: Bottles of beer
"""

import argparse
from typing import Final


TAKE_ONE_DOWN: Final = 'Take one down, pass it around,'


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    _ = [print(verse(bottle) + ("\n" if bottle > 1 else ""))
         for bottle in range(args.num, 0, -1)]


# --------------------------------------------------
def verse(bottle: int):
    """Sing a verse"""

    return '\n'.join([
        f'{plural(bottle)} of beer on the wall,',
        f'{plural(bottle)} of beer,',
        TAKE_ONE_DOWN,
        'No more bottles of beer on the wall!'
           if bottle-1 == 0 else f'{plural(bottle-1)} of beer on the wall!'
        ])


def plural(bottle: int):
    """Help me out with plural of bottle(s)"""
    return f'{bottle} bottle{"s" if bottle > 1 else ""}'


def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,',
        '1 bottle of beer,',
        TAKE_ONE_DOWN,
        'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,',
        '2 bottles of beer,',
        TAKE_ONE_DOWN,
        '1 bottle of beer on the wall!'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
