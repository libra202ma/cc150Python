"""
You are given two 32-bit number, N and M, and two bit positions, i
and j. Write a method to insert M into N such that M starts at bit j
and ends at bit i. You can assume that the bits j through i have
enough space to fit all of M. That is, if M = 10011, you can assume
that there are at least 5 bits between j and i. You would not, for
example, have j = 3 and i = 2, because M could not fully fit between 3
and 2.

EXAMPLE
Input:  N = 10000000000, M = 10011, i = 2, j = 6
Output: N = 10001001100

- update Bits. Firstly clear bits [i:j] in N, using AND masks
like 1111000111. Then shift M to [i, j], perform an OR operation on N.
"""


def insert(N, M, i, j):
    # clear bits from i to j
    clearmask = 0
    for k in range(i, j+1):
        clearmask += 1 << k
    clearmask = ~clearmask
    N &= clearmask

    # set bits
    N |= M << i
    return N


def test_insert():
    N = 0b10000000000
    M = 0b10011
    i = 2
    j = 6
    assert insert(N, M, i, j) == 0b10001001100
