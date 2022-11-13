#!/usr/bin/env python3
"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2022-11-13
Purpose: Telephone
"""

import argparse
import os
import io
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text, encoding='utf-8')
    else:
        args.text = io.StringIO(args.text + '\n')

    if args.mutations < 0.0 or args.mutations > 1.0:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    for line in args.text:
        text = line.rstrip()
        alpha = "".join(sorted(string.ascii_letters + string.punctuation))
        num_mutations = round(len(text) * args.mutations)

        indexes = random.sample(list(range(len(text))), num_mutations)

        heard = text[:]
        for i in indexes:
            new_char = random.choice(alpha.replace(heard[i], ''))
            heard = heard[:i] + new_char + heard[i+1:]

        print(f'You said: "{text}"')
        print(f'I heard : "{heard}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
