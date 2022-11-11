#!/usr/bin/env python3
"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2022-11-11
Purpose: Jump the five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the five -- you may not understand',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('message',
                        metavar='str',
                        help='message to obfuscate')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    message = args.message

    jumper = {'0': '5', '1': '9', '2': '8', '3': '7', '4': '6',
              '5': '0', '6': '4', '7': '3', '8': '2', '9': '1'}

    jumped = [jumper[k] if k in jumper else k for k in message]
    print("".join(jumped))


# --------------------------------------------------
if __name__ == '__main__':
    main()
