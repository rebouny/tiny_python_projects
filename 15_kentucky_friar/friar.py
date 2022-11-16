#!/usr/bin/env python3
"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2022-11-16
Purpose: Kentucky Friar
"""

import argparse
import os
import io
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Southern fry text',
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
        print(''.join(map(fry, re.split(r'(\W+)', text.rstrip()))))


# --------------------------------------------------
def fry(word):
    "Frys a single word"
    matched = re.match(r'^([yY])ou$', word)
    if matched:
        return matched.group(1) + "'all"

    matched = re.match(r'((\w+)in)g$', word)
    if matched and re.search(r'[aeiouAEIOU]', matched.group(2)):
        return matched.group(1) + "'"

    return word


def test_fry():
    """Tests fryer"""
    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('fishing') == "fishin'"
    assert fry('Aching') == "Achin'"
    assert fry('swing') == "swing"


# --------------------------------------------------
if __name__ == '__main__':
    main()
