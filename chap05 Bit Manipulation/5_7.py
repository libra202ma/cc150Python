"""
An array A contains all the integers from 0 to n, except for one
number which is missing. In this problem, we cannot access an entire
integer in A with a single operation. The elements of A are
represented in binary, and the only operation we can use to access
them is "fetch the j-th bit of A[i]", which takes constant time. Write
code to find the missing integer. Can you do it in O(n) time?

- Scan the least significant bit of every integers in A. It should be
0, 1, 0, 1, .... The missing of an integer will cause two conccessive
0s or 1s.
"""


def findmissing(arr):
    lastbit = 1
    for i, n in enumerate(arr):
        bit = n & 1
        if bit == lastbit:
            return n - 1
        else:
            lastbit = bit


def test_findmissing():
    arr = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10]
    assert findmissing(arr) == 7
