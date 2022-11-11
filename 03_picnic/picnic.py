#!/usr/bin/env python3
"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2022-11-11
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic -- sort what you have',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        help='one or more items to bring with',
                        type=str,
                        nargs='+')

    parser.add_argument('-s',
                        '--sorted',
                        help='if list shall be sorted',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = sorted(args.items) if args.sorted else args.items
    if len(items) > 1:
        items[-1] = f"and {items[-1]}"

    listings = ", ".join(items) if len(items) > 2 else " ".join(items)
    print(f"You are bringing {listings}.")


# --------------------------------------------------
if __name__ == '__main__':
    main()
