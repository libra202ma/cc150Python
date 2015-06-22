"""
Given a positive integer, print the next smallest and the next
largest number that have the same number of 1 bits in their binary
representation.

- Scan from right to left to find the smallest 1,, then move to right
to find an 0, if we found, then swap the 1 and 0, if not found, scan
from last stopped point to find another 1. (?)

To find the next bigger number, we scan for 0 and try to swap it with
an 1 on its right. (?)

- Arithmaetic approach based on previous approach.
"""


def nextlarger(n):
    n = list(bin(n)[2:])  # string, binary representation of n
    start1s = len(n) - 1 # index of start of trailing 1s
    while n[start1s] == '0':
        start1s -= 1
    # now start1s point to end of trailing 1s
    while n[start1s] == '1':
        start1s -= 1
    start1s += 1
    # now start1s point to start of trailing 1s
    n[start1s - 1] = '1'
    n[start1s] = '0'
    # set the last non-trailing 0 to 1
    # to keep the number of 1, set the start of trailing 1s to 0
    # then move the other 1s to end to keep the number as small as possible
    start1s += 1
    end = len(n) - 1
    while start1s < end and n[start1s] == '1' and n[end] == '0':
        n[start1s] = '0'
        n[end] = '1'
        start1s += 1
        end -= 1

    return int(''.join(n), base=2)


def test_nextlarger():
    assert nextlarger(0b11011001111100) == 0b11011010001111



def nextlargerArith(n):
    nbin = bin(n)[2:]
    c0 = 0
    p = len(nbin) - 1
    while nbin[p] == '0':
        c0 += 1
        p -= 1
    # now p point to last 1
    c1 = 0
    while nbin[p] == '1':
        c1 += 1
        p -= 1
    # now p point to last non-trailing 0
    return n + 2**c0 + 2**(c1 - 1) - 1

def test_nextlargerArith():
    assert nextlargerArith(0b11011001111100) == 0b11011010001111
