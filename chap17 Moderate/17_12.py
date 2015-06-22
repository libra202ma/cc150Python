"""
Design an algorithm to find all pairs of integers within an array
which sum to a specific value.

HashSet. O(n).

"""


def findPairs(l, theSum):
    s = set()
    ret = []
    for n in l:
        if theSum - n in s:
            ret.append([theSum - n, n])
        else:
            s.add(n)
    return ret


def test_findPairs():
    assert findPairs([1, 2, 3, 4, 5, 6, 7], 7) == [[3, 4], [2, 5], [1, 6]]
