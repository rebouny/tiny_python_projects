#!/usr/bin/env python3
"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2022-11-14
Purpose: Rhyming Words
"""

import argparse
import re
import string
from typing import Final


CONSONANTS: Final = "".join(
    filter(lambda x: x not in 'aeiou', string.ascii_lowercase)
    )

CLUSTER: Final = [
    'bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr',
    'pl', 'pr', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st',
    'sw', 'th', 'tr', 'tw', 'thw', 'wh', 'wr', 'sch', 'scr', 'shr',
    'sph', 'spl', 'spr', 'squ', 'str', 'thr'
    ]


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        type=str,
                        help='A word to rhyme')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    (drop, stem) = stemmer(args.word)

    if stem:
        _ = [print(f'{x}{stem}') for x in sorted([*CONSONANTS, *CLUSTER])
             if x != drop]
    else:
        print(f'Cannot rhyme "{args.word}"')


# --------------------------------------------------
def stemmer(word: str):
    """Return leading consonants (if any), and 'stem' of word"""
    regex = re.compile(f'([{CONSONANTS}]+)?([aeiou].*)')
    matched = regex.match(word.lower())

    if not matched:
        return (word.lower(), '')

    return (
        matched.group(1) or '',
        matched.group(2) or ''
    )


def test_stemmer():
    """ Test stemmer """
    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')
    assert stemmer('123') == ('123', '')


# --------------------------------------------------
if __name__ == '__main__':
    main()
