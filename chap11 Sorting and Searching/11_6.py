# -*- coding: utf-8; -*-

"""
Given an MxN matrix in which each row and each column is sorted in
an ascending order, write a method to find an element.

- Two dimensional Binary search.

From the condition that the matrix is sorted both in column and row
order, the following conclusion could be made:

- the diagonal of the matrix is sorted.
- the upper left corner is smallest and lower right corner largest.

If the target could be found on the diagonal, then return the
location, If not, i.e., the target larger than (i, j) but smaller than
(i+1, j+1), we continue search upper right corner and lower left
corner.
"""

import numpy

# here we import numpy module to use the numpy.ndarray type, since
# python's built-in list does not support well of multi-dimensional
# array slicing. For example, say a matrix M[N][N], the slicing
# M[i:j][i:j] does not give us what when wanted, i.e., a submatrix,
# but instead Python interpret it as M[i:j] rows, and then select
# [i:j] from the list of rows.

def searchMatrixDiagonal(M, rstart, rend, cstart, cend, target):
    """
    Search matrix diagonal

    Modification of one-dimension binary search. Return the index such
    that M[ridx, cidx] <= target < L[ridx + 1, cidx + 1]
    """
    assert type(M) == numpy.ndarray

    if rstart > rend or cstart > cend:
        return None

    # return early if the target is not possible in this range
    if M[rstart, cstart] > target:
        return None
    if M[rend, cend] < target:
        return None

    # the matrix might not be square, fix this
    diaglen = min(rend - rstart, cend - cstart)
    rend = rstart + diaglen
    cend = cstart + diaglen
    rmid = (rstart + rend) / 2
    cmid = (cstart + cend) / 2

    if rmid + 1 >= M.shape[0] or cmid + 1 >= M.shape[1]:
        # there is only one item in diagonal
        return (rmid, cmid)
    elif M[rmid, cmid] <= target and target < M[rmid + 1, cmid + 1]:
        return (rmid, cmid)
    elif target >= M[rmid + 1, cmid + 1]:
        return searchMatrixDiagonal(M, rmid + 1, rend, cmid + 1, cend, target)
    else:
        return searchMatrixDiagonal(M, rstart, rmid - 1, cstart, cmid - 1, target)

def test_searchMatrixDiagonal():
    M = numpy.array([
        [15, 20, 70, 85],
        [25, 35, 80, 95],
        [30, 55, 95, 105],
        [40, 80, 100, 120]
    ])

    assert searchMatrixDiagonal(M, 0, 3, 0, 3, 10) == None
    assert searchMatrixDiagonal(M, 0, 3, 0, 3, 35) == (1, 1)
    assert searchMatrixDiagonal(M, 0, 3, 0, 3, 55) == (1, 1)
    assert searchMatrixDiagonal(M, 0, 3, 0, 3, 120) == (3, 3)
    assert searchMatrixDiagonal(M, 0, 3, 0, 3, 150) == None


# matrix search range is specified by four parameter, left upper
# corner and lower right corner, or row start, row end, column start
# and column end.
def searchMatrixHelper(M, rstart, rend, cstart, cend, target):
    assert type(M) == numpy.ndarray
    print 'searching in'
    print M[rstart:rend+1, cstart:cend+1]

    # search in diagonal
    didx = searchMatrixDiagonal(M, rstart, rend, cstart, cend, target)
    if didx is None:
        return None
    elif M[didx] == target:
        return didx
    else:
        ridx, cidx = didx
        # search lower left corner
        idx = searchMatrixHelper(M, cidx + 1, rend, cstart, cidx, target)
        if idx is not None:
            return idx
        else:
            return searchMatrixHelper(M, rstart, ridx, cidx + 1, cend, target)


def searchMatrix(M, target):
    return searchMatrixHelper(M, 0, M.shape[0] - 1, 0, M.shape[1] - 1, target)


def test_searchMatrix():
    M = numpy.array([
        [15, 20, 70, 85],
        [25, 35, 80, 95],
        [30, 55, 95, 105],
        [40, 80, 100, 120]
    ])

    assert searchMatrix(M, 55) == (2, 1)
    assert searchMatrix(M, 70) == (0, 2)
    assert searchMatrix(M, 99) == None
