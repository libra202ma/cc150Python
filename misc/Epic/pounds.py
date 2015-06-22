# coding: utf-8

"""
你有无限多个3磅，7磅，16磅的砝码，找到最短的组合达到目标X磅，如果没有这样的组合，返回0。

Greedy algorithm 不可行. 例如, 24 应该返回 (7, 7, 7, 3).
"""


def pounds(n):
    if n == 0:
        return []
    elif n < 0:
        return -1

    for d in [16, 7, 3]:
        path = pounds(n - d)
        if path != -1:
            path.insert(0, d)
            return path

    return -1


def test_pounds():
    assert pounds(24) == [7, 7, 7, 3]
    assert pounds(5) == -1
