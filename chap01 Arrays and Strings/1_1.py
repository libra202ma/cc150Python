#!/usr/bin/env python

"""
Implement an algorithm to determine if a string has all unique
characters.  What if you cannot use additional data structures?

Ask about characters? ASCII?

- naive. for every character, scan and log.
- improve by using bit array.
- sort and check neighbors.
"""

# assume ASCII characters

def isuniqueList(str):
    if len(str) > 128:
        # pigeon hole principle
        return False

    charlist = [0] * 128
    for c in str:
        idx = ord(c)
        if charlist[idx] == 1:
            return False
        else:
            charlist[idx] = 1

    return True


def test_isuniqueList():
    assert isuniqueList("OK") == True
    assert isuniqueList("HAHA") == False


def isuniqueHash():
    if len(str) > 128:
        return False

    charset = {}
    for c in str:
        if c in charset:
            return False
        else:
            charset[c] == 1

    return True



def test_isuniqueHash():
    assert isuniqueList("OK") == True
    assert isuniqueList("HAHA") == False
