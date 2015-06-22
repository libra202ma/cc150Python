"""
Write a method to return all subsets of a set.

- recursion. subsets of S(A1, ..., An) = subsets of S(A1, ...,
A_{n-1}) * An U subsets of S(A1, ..., A_{n-1})
"""


def getsubsets(s):
    """
    return list of lists
    """
    if s == []:
        return [[]]

    subsets1 = getsubsets(s[:-1])
    subsets2 = []
    for subset in subsets1:
        subsets2.append(subset + [s[-1]])

    return subsets1 + subsets2


def test_getsubsets():
    assert getsubsets([]) == [[]]
    assert getsubsets([1]) == [[], [1]]
    assert getsubsets([1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

