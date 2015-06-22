#!/usr/bin/env python

"""
Implement a method to perform basic string compression using the
counts of repeated characters. For example, the string aabcccccaaa
would become a2b1c5a3. If the "compressed" string would not become
smaller that the original string, your method should return the
origial string.

- naive. Create new buffer, scan and count.
- improve by calculate size needed for new string and pre-allocate buffer for
  new string, only needed for C.
"""


def compress(string):
    newstring = ''
    lastchar = string[0]
    count = 1
    for char in string[1:]:
        if char == lastchar:
            count += 1
        else:
            newstring += lastchar + str(count)
            lastchar = char
            count = 1
    newstring += lastchar + str(count)

    if len(newstring) < string:
        return newstring
    else:
        return string



def test_compress():
    assert compress('aaa') == 'a3'
    assert compress('aabcccccaaa') == 'a2b1c5a3'
