#!/usr/bin/env python3
"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2022-11-17
Purpose: Mad Libs
"""

import argparse
import sys
import re
from typing import Final

RE_TAGS: Final = r'(<([^<>]+)>)'


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs (for testing)',
                        metavar='input',
                        type=str,
                        nargs='*',
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    inputs = args.inputs

    text = args.FILE.read().strip()
    matches = re.findall(RE_TAGS, text)

    if not matches:
        sys.exit(f'"{args.FILE.name}" has no placeholders.')

    for placeholder, name in matches:
        article = 'an' if name[0].lower() in 'aeiou' else 'a'
        in_str = inputs.pop(0) if inputs \
            else input(f'Give me {article} {name}: ')
        text = re.sub(placeholder, in_str, text, 1)

    print(text)


# --------------------------------------------------


# --------------------------------------------------
if __name__ == '__main__':
    main()
