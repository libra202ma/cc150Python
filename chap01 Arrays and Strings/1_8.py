#!/usr/bin/env python

"""
Assume you have a method isSubstring which checks if one word is a
substring of another. Given two strings, s1 and s2, write code to
check if s2 is a rotation of s1 using only one call to isSubstring
(e.g., "watterbottle" is a rotation of "erbottlewat").

- assume s1 = XY, s2 = YX, if s2 is a rotation of s1, it must be a
substring of XYXY, i.e., s1 + s1.
"""


def issubstring(substring, string):
    """Test if substring is a substring of string"""
    return substring in string


def test_issubstring():
    assert issubstring("Py", "Python") == True
    assert issubstring("py", "Python") == False


def isrotation(s1, s2):
    return issubstring(s2, s1 + s1)


def test_isrotation():
    assert isrotation("watterbottle", "erbottlewat") == True
