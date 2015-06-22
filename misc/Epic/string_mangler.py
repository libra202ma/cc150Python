# coding: utf-8

"""
String Mangler。给你一个字符串S，把所有元音字母变成大写，所有不是word最后一个字符的辅音字母变小写，所有word的最后一个字母变大写。
"""


def mangler(s):
    wordlist = s.split(' ')
    newstr = []
    for word in wordlist:
        for (ci, c) in enumerate(word):
            if c in ['a', 'e', 'i', 'o', 'u']:
                newstr.append(c.upper())
            elif ci == len(word) - 1:
                newstr.append(c.upper())
            else:
                newstr.append(c.lower())
        newstr.append(' ')

    return ''.join(newstr)[:-1]


def test_mangler():
    assert mangler("Kind of Fun") == "kInD OF fUN"
