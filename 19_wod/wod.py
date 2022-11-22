#!/usr/bin/env python3
"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2022-11-22
Purpose: Workout of the day
"""

import argparse
import random
import csv
import sys
import io
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='./inputs/exercises.csv')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='exercises',
                        type=int,
                        default=4)

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    all_exercises = read_csv(args.file)
    if len(all_exercises) == 0:
        sys.exit(f"No usable dat in --file '{args.file}'")
    len_exercises = len(all_exercises)
    if len_exercises < args.num:
        sys.exit(f'--num "{args.num}" > exercises "{len_exercises}"')

    selected_exercises = random.sample(all_exercises, k=args.num)

    print(tabulate(make_wod(selected_exercises, args.easy),
                   headers=('Exercise', 'Reps')))


# --------------------------------------------------
def make_wod(selected_exercises, easy):
    """Selects a workout of the day"""
    wod = []

    for exercise, low, high in selected_exercises:
        reps = random.randint(low, high)
        if easy:
            reps = int(reps/2)
        wod.append((exercise, reps))

    return wod


def read_csv(file_handle):
    """Read the CSV input"""
    reader = csv.DictReader(file_handle, delimiter=',')
    exercises = []
    for rec in reader:
        name, reps = rec.get('exercise'), rec.get('reps')
        if not name or not reps:
            continue
        low, high = map(int, reps.split('-'))
        exercises.append((name, low, high))

    return exercises


def test_read_csv():
    """Test read_csv"""
    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(text) == [('Burpees', 20, 50), ('Situps', 40, 100)]


# --------------------------------------------------
if __name__ == '__main__':
    main()
