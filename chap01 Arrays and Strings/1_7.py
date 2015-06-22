#!/usr/bin/env python

"""
Write an algorithm such that if an element in a MxN matrix is 0,
its entire row and column are set to 0.

- naive. log rows and columns to be set first using set, then set the
rows and columns.
"""


def setzeros(mat):
    M = len(mat)
    N = len(mat[0])
    rows = []
    columns = []
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 0:
                rows.append(i)
                columns.append(j)

    for i in rows:
        for j in range(N):
            mat[i][j] = 0
    for j in columns:
        for i in range(M):
            mat[i][j] = 0



def test_setzeros():
    M = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    setzeros(M)
    assert M == [[1, 0, 3], [0, 0, 0], [7, 0, 9]]
