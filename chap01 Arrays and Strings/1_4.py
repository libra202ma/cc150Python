#!/usr/bin/env python

"""
Write a method to replace all spaces in a string with "%20". You
may assume that the string has sufficient space at the end of the
string to hold additional characters, and you are given the "true"
length of the string.  (Note: if implementing in Java, please use a
character array so that you can perform this operation in place.)

EXAMPLE
Input: "Mr John Smith     "
Output: "Mr%20John%20Smith"

- naive. work backwards.
"""


def replaceSpaces(s):
    i = len(s) - 1
    while s[i] == ' ':
        i -= 1
    # i now point to the last character that is not space
    j = len(s - 1)
    while i >= 0:
        if s[i] == ' ':
            s[j-2:j+1] = '%20'
            j -= 3
        else:
            s[j] = s[i]
        i -= 1



def test_replaceSpaces():
    s = "Mr John Smith     "
    replaceSpaces(s)
    assert s == "Mr%20John%20Smith"
