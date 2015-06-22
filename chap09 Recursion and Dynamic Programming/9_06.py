"""
Implement an algorithm to print all valid (e.g., properly opened
and closed) combinations of n-pairs of parentheses.

EXAMPLE
Input: 3
Output: ((())), (()()), (())(), ()(()), ()()()

For n-pair
- place n-th pair parallel on left or right side of n-1 pairs
- enclose any item of all n-1 pairs
"""

def parentheses(n):
    if n == 1:
        return set(['()'])

    ret = set()
    subret = parentheses(n - 1)
    for p in subret:
        ret.add(p + '()')
        ret.add('()' + p)
        ret.add('(' + p + ')')

    return ret


def test_parentheses():
    assert parentheses(3) == set(['()()()', '(()())', '(())()', '()(())', '((()))'])
