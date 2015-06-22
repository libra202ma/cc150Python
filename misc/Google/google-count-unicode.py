# -*- coding: utf-8; -*-

"""
0. Talk about favourite programming languages and why choose them.
1. Coding question of my phone interview of Google. Count unicode
characters in a byte array.
"""

"""
Counting unicode characters
"""

def count1s(byte):
    """
    count number of leading 1s of a byte

    for ASCII characters, it should be 0
    for Unicode characters, it should be greater than or equal to 2
    """
    bitidx = 0
    cnt = 0
    while byte << bitidx >> 7 & 1:
        cnt += 1
        bitidx += 1
    return cnt


def test_count1s():
    assert count1s(0b01111111) == 0
    assert count1s(0b10111111) == 1
    assert count1s(0b11011111) == 2


def countunicode(bytes):
    cnt = 0
    n1s = 0
    for i in range(len(bytes)):
        print i, cnt, n1s
        if n1s == 0:
            n1s = count1s(bytes[i])
            cnt += 1
            if n1s != 0:
                # if the number of leading 1 is greater than 1, then
                # we use n1s as marks to check the following bytes
                n1s -= 1
        else:
            if count1s(bytes[i]) != 1:
                raise UnicodeError("Invalid unicode string")
            else:
                n1s -= 1

    return cnt


def test_countunicode():
    assert countunicode([0b00100100]) == 1
    assert countunicode([0b11000010, 0b10100010]) == 1
    assert countunicode([\
                         0b00100100, \
                         0b11000010, 0b10100010, \
                         0b11100010, 0b10000010, 0b10101100 \
                     ]) == 3
    assert countunicode( \
                         [ord(c) for c in list("人生来就不平等")] \
                     ) == 7
