#!/usr/bin/env python3
"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2022-11-26
Purpose: Tic-Tac-Toe
"""

import argparse
import re
from typing import List


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--board',
                        help='The state of the board',
                        metavar='board',
                        default='.' * 9,
                        type=str)

    parser.add_argument('-c',
                        '--cell',
                        help='Cell 1-9',
                        metavar='cell',
                        type=int,
                        choices=range(1, 10),
                        default=None)

    parser.add_argument('-p',
                        '--player',
                        help='Player',
                        metavar='player',
                        type=str,
                        choices=['X', 'O'],
                        default=None)

    args = parser.parse_args()

    if (args.cell and not args.player) or (args.player and not args.cell):
        # could use 'any' and 'not all' instead
        parser.error('Must provide both --player and --cell')

    if len(args.board) != 9 or re.match('[^.OX]', args.board):
        parser.error(f'--board "{args.board}" must be 9 characters of ., C, O')

    if args.cell and args.board[args.cell-1] != '.':
        parser.error(f'--cell "{args.cell}" already taken')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    board = list(args.board)

    if args.player:
        board[args.cell - 1] = args.player

    print(format_board(board))
    winner = find_winner(board)
    print(f'"{winner}" has won!' if winner else 'No winner')


# --------------------------------------------------
def find_winner(board: List[str]):
    """Returns the winning player of a board, None if there is no one"""
    winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
               [0, 3, 6], [1, 4, 7], [2, 5, 8],
               [0, 4, 8], [2, 4, 6]]

    for player in 'XO':
        for i, j, k in winning:
            if ''.join([board[i], board[j], board[k]]) == player * 3:
                return player

    return None


def format_board(board: List[str]):
    """Returns string representation of the board"""

    cells = [str(i) if c == '.' else board[i-1]
             for i, c in enumerate(board, start=1)]

    horizontal_rule = '-' * 13

    return (f'{horizontal_rule}\n'
            f'| {cells[0]} | {cells[1]} | {cells[2]} |\n'
            f'{horizontal_rule}\n'
            f'| {cells[3]} | {cells[4]} | {cells[5]} |\n'
            f'{horizontal_rule}\n'
            f'| {cells[6]} | {cells[7]} | {cells[8]} |\n'
            f'{horizontal_rule}'
            )


# --------------------------------------------------
if __name__ == '__main__':
    main()
