"""
Design an algorithm to figure out if someone has won a game of
tic-tac-toe.

Just brute-force.

For multi-time calling, calculate all possible win cases. For every
query, just check if the current state is one of the win cases.
"""

import numpy as np


def isWon(board, player):
    # check horizontal
    for i in range(3):
        for j in range(3):
            if board[i, j] != player:
                break
        else:
                return True

    # check vertical
    for j in range(3):
        for i in range(3):
            if board[i, j] != player:
                break
        else:
            return True

    # check diagonal
    for i in range(3):
        if board[i, i] != player:
            break
    else:
        return True
    for i in range(3):
        if board[i, 3 - 1 - i]:
            break
    else:
        return True

    # not won
    return False


def isSomeoneWon(board):
    if isWon(board, 'O') or isWon(board, 'X'):
        return True
    else:
        return False


def test_isSomeoneWon():
    board = np.array([
        [' ', 'X', ' '],
        ['O', 'X', 'O'],
        ['O', 'X', 'O'],
    ])
    assert isWon(board, 'X') is True
    assert isWon(board, 'O') is False
    assert isSomeoneWon(board) is True
