"""
Given a boolean expression consisting of the symbols 0, 1, &, |,
and ^, and a desired boolean result value result, implement a function
to count the number of ways of parenthesizing the expression such that
it evaluates to result.

EXAMPLE

Expression: 1 ^ 0 | 0 | 1
Desired result: false (0)
Output: 2 ways. 1 ^ ((0 | 0) | 1) and 1 ^ (0 | (0 | 1))
"""

def countways(exp, target):
    exp = exp.replace(' ', '')
    if len(exp) == 1:
        # ('1', 1) -> 1
        # ('1', 0) -> 0
        # ('0', 1) -> 0
        # ('0', 0) -> 1
        return 1 - (int(exp) ^ target)

    cnt = 0
    if target == 1:
        for i, op in enumerate(exp):
            if op == '&':
                cnt += countways(exp[:i], 1) * countways(exp[i+1:], 1)
            elif op == '|':
                cnt += countways(exp[:i], 1) * countways(exp[i+1:], 0) + \
                       countways(exp[:i], 0) * countways(exp[i+1:], 1) + \
                       countways(exp[:i], 1) * countways(exp[i+1:], 1)
            elif op == '^':
                cnt += countways(exp[:i], 1) * countways(exp[i+1:], 0) + \
                       countways(exp[:i], 0) * countways(exp[i+1:], 1)
    else:
        for i, op in enumerate(exp):
            if op == '&':
                cnt += countways(exp[:i], 0) * countways(exp[i+1:], 0) + \
                       countways(exp[:i], 1) * countways(exp[i+1:], 0) + \
                       countways(exp[:i], 0) * countways(exp[i+1:], 1)
            elif op == '|':
                cnt += countways(exp[:i], 0) * countways(exp[i+1:], 0)
            elif op == '^':
                cnt += countways(exp[:i], 1) * countways(exp[i+1:], 1) + \
                       countways(exp[:i], 0) * countways(exp[i+1:], 0)

    return cnt

def test_countways():
    # assert countways('1', 1) == 1
    # assert countways('1', 0) == 0
    # assert countways('0', 1) == 0
    # assert countways('0', 0) == 1
    assert countways('1 ^ 0 | 0 | 1', 0) == 2
