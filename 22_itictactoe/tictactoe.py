#!/usr/bin/env python3
"""
Author : Martin Schuh <development@rebouny.net>
Date   : 2022-11-26
Purpose: Tic-Tac-Toe (interactive)
"""

from typing import List, NamedTuple, Optional
import re


class State(NamedTuple):
    """Container for storing game state"""
    board: List[str] = list('.' * 9)
    player: str = 'X'
    quit: bool = False
    draw: bool = False
    error: Optional[str] = None
    winner: Optional[str] = None


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    state = State()

    while not any([state.quit, state.draw, state.winner]):
        board = state.board
        print(format_board(board))

        move = input(f'Player "{state.player}", what is your move? '
                     '[q to quit]: ')
        if not re.match(r'[1-9q]', move):
            print(f'Invalid cell "{move}", please use 1-9')
            continue

        if move == 'q':
            state = state._replace(quit=True, error=False)
            continue

        if board[int(move) - 1] in 'XO':
            print(f'Cell "{move}" already taken')
            state = state._replace(error=True)
            continue

        board[int(move) - 1] = state.player

        # get next player
        player = 'O' if state.player == 'X' else 'X'
        winner = find_winner(board)
        draw = not winner and all(map(lambda i: i in 'XO', board))
        state = state._replace(board=board, player=player,
                               winner=winner, draw=draw)

    if not state.quit:
        print(format_board(state.board))
    if state.winner:
        print(f'"{state.winner}" has won!')
    if state.draw:
        print("It's a draw!")


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


def format_board(board: List[str]) -> str:
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
