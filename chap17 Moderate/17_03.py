"""
Write an algorithm which computes the number of trailing zeros in
n factorial.

Count number of 5. Since 5 is less than 2.

"""

from functools import lru_cache


# cache results
@lru_cache(maxsize=None)
def count5s(n):
    cnt = 0
    while n > 0 and n % 5 == 0:
        return cnt + 1 + count5s(n//5)
    return cnt


def test_count5s():
    assert count5s(1) == 0
    assert count5s(25) == 2
    assert count5s(125) == 3


def countFactorialZeros(n):
    cnt = 0
    for i in range(1, n+1):
        cnt += count5s(i)
    return cnt


def test_countFactorialZeros():
    assert countFactorialZeros(5) == 1
    assert countFactorialZeros(17) == 3
    assert countFactorialZeros(30) == 7
