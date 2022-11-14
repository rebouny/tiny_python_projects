#!/usr/bin/env python3
"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2022-11-14
Purpose: Twelve Days
"""

import argparse
import sys
from typing import Final

ORDINAL: Final = {
    1: 'first',
    2: 'second',
    3: 'third',
    4: 'fourth',
    5: 'fifth',
    6: 'sixth',
    7: 'seventh',
    8: 'eighth',
    9: 'ninth',
    10: 'tenth',
    11: 'eleventh',
    12: 'twelfth'
}

GIFTS: Final = {
    1: 'A partridge in a pear tree.',
    2: 'Two turtle doves,',
    3: 'Three French hens,',
    4: 'Four calling birds,',
    5: 'Five gold rings,',
    6: 'Six geese a laying,',
    7: 'Seven swans a swimming,',
    8: 'Eight maids a milking,',
    9: 'Nine ladies dancing,',
    10: 'Ten lords a leaping,',
    11: 'Eleven pipers piping,',
    12: 'Twelve drummers drumming,'
}

MY_DEAR_LOVE: Final = 'My true love gave to me,'


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()

    if args.num < 1 or args.num > 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    args.outfile.write("\n\n".join(map(verse, range(1, args.num + 1))))
    args.outfile.write("\n")
    args.outfile.close()


# --------------------------------------------------
def verse(day: int):
    """Create a verse"""

    verces = [
        f'On the {ORDINAL.get(day, day)} day of Christmas,',
        MY_DEAR_LOVE,
    ]
    verces.extend([f'{GIFTS[count]}' for count in range(day, 0, -1)])

    if day != 1:
        verces[-1] = f"And {verces[-1][0].lower()}{verces[-1][1:]}"

    return "\n".join(verces)


def test_verse():
    """Test verse"""
    assert verse(1) == '\n'.join([
        'On the first day of Christmas,',
        MY_DEAR_LOVE,
        'A partridge in a pear tree.'
    ])

    assert verse(2) == '\n'.join([
        'On the second day of Christmas,',
        MY_DEAR_LOVE,
        'Two turtle doves,',
        'And a partridge in a pear tree.'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
