"""
A magic index in an array A[1...n-1] is defined to be an index
such that A[i] = i. Given a sorted array of distinct integers, write a
method to find a magic index, if one exists, in array A.

FOLLOW UP

What if the values are not distinct?

- naive.
- Binary search / Recursion.
"""

def magicHelper(A, i, j):
    if i > j:
        return None

    mid = (i + j) / 2
    if A[mid] == mid:
        return mid
    elif A[mid] < mid:
        return magicHelper(A, mid + 1, j)
    else:
        return magicHelper(A, i, mid - 1)

def magic(A):
    return magicHelper(A, 0, len(A) - 1)


def test_magic():
    assert magic([0]) == 0
    assert magic([1]) == None
    assert magic([-2, -1, 2, 7]) == 2
