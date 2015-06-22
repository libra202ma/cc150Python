"""
Write a method to compute all permutations of a string.

- recursion. The permutation of string is any character + permutation
of substring without the character. Alternatively, by pushing the last
character into every possible location in substring.
"""

def permutation(string):
    if len(string) == 1:
        return [string]

    pmtt = []
    for c in string:
        pmttsub = permutation(string.replace(c, ''))
        for s in pmttsub:
            pmtt.append(c + s)

    return pmtt

def test_permutation():
    assert permutation('a') == ['a']
    assert permutation('ok') == ['ok', 'ko']
    assert permutation('abc') == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

