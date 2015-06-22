"""
Design a method to find the frequency of occurrences of any given
word in a book.

Dict.
"""


def countFreq(book, word):
    freq = {}
    freq.setdefault(0)
    for word in book:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
    return freq[word]


def test_countFreq():
    assert countFreq([
        'men',
        'do',
        'not',
        'born',
        'equally',
        'men'
    ], 'men') == 2
