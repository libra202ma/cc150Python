#!/usr/bin/env python

"""
Given two strings, write a method to decide if one is a
permutation of the other.

Ask about characters set? ASCII?

- naive. sort then compare.
- count characters and compare.
"""

def ispermutationSort(s1, s2):
    if len(s1) != len(s2):
        # if the strings are not same length, they cannot be
        # permutations
        return False

    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


def test_ispermutationSort():
    assert ispermutationSort("naive", "inave") == True
    assert ispermutationSort("hello", "world") == False


def count(s):
    charset = {}
    for c in s:
        if c in charset:
            charset[c] += 1
        else:
            charset[c] = 1
    return charset


def ispermutationCount(s1, s2):
    if len(s1) != len(s2):
        return False

    if count(s1) == count(s2):
        return True
    else:
        return False


def test_ispermutationCount():
    assert ispermutationCount("naive", "inave") == True
    assert ispermutationCount("hello", "world") == False
