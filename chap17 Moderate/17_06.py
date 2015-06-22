"""
Given an array of integers, write a method to find indices m and n
such that if you sorted elements m though n, the entire array would be
sorted. Minimize n - m (that is, find the smallest such sequence).

EXAMPLE
Input: 1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19
Output: (3, 9)

Brute-force.

Find the bound that breaks increasing trend. Find the min and max
within this range. Then use binary search to find the locations that
those min and max should be.

To optimize, the boundaries could be found by using a exponential
increasing step.
"""


def left(l):
    """
    Find the left index of un-increasing part.
    """
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            break
    return i + 1


def right(l):
    """
    Find the right index of un-increasing part.
    """
    for i in range(len(l) - 2, 0, -1):
        if l[i] > l[i + 1]:
            break
    return i


def binarySearch(l, left, right, n):
    """
    Find the index n should be.
    """
    if left == right:
        return left

    mid = (left + right)//2
    if l[mid] <= n < l[mid + 1]:
        return mid
    elif n < l[mid]:
        return binarySearch(l, left, mid, n)
    else:
        return binarySearch(l, mid + 1, right, n)


def test_binarySearch():
    assert binarySearch([1, 3, 5], 0, 2, 2) == 0
    assert binarySearch([1, 3, 5], 0, 2, 3) == 1
    assert binarySearch([1, 3, 5], 0, 2, 1) == 0
    assert binarySearch([1, 3, 5], 0, 2, 0) == 0
    assert binarySearch([1, 3, 5], 0, 2, 7) == 2


def findRange(l):
    """
    Find the minimal part of array should be changed in sorting.
    """
    leftidx = left(l)
    rightidx = right(l)
    minm = min(l[leftidx:rightidx + 1])
    maxm = max(l[leftidx:rightidx + 1])

    leftidx = binarySearch(l, 0, leftidx, minm)
    rightidx = binarySearch(l, rightidx, len(l), maxm)

    return (leftidx, rightidx)


def test_findRange():
    assert findRange([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]) == (3, 9)
