"""

Problem from one of my housemate's interview with Morgan Stanley at 2013.

"""

denoms = [1, 5, 10, 25]

def nchanges(n, denoms=denoms):
    "Recursive. Top down"

    print()
    print("nchanges(", n, ", ", denoms, ")")

    if denoms == [1]:
        return 1

    cnt = 0
    d = denoms[-1]
    # i = 0, means do not use the largest coin, use only smaller ones
    # i = 1, ..., n//d, means use i largest coins
    for i in range(n//d + 1):
        cnt += nchanges(n - d * i, denoms[:-1])

    return cnt


def test_nchanges():
    assert nchanges(1) == 1
    assert nchanges(5) == 2
    assert nchanges(6) == 2
    assert nchanges(10) == 4
    assert nchanges(15) == 6

import numpy as np

def nchangesD(n, denoms=denoms):
    "Dynamic programming. Bottom up."
    tbl = np.ones((n+1, len(denoms)), dtype=int)
    for m in range(1, n+1):
        for (i, d) in enumerate(denoms):
            if i == 0:  # the smallest denom
                changesSmaller = 0
            else:
                changesSmaller = tbl[m, i - 1]

            if m - d < 0:
                changesLess = 0
            else:
                changesLess = tbl[m - d, i]

            tbl[m, i] = changesSmaller + changesLess

    return tbl[n, -1]


def test_nchangesD():
    assert nchangesD(1) == 1
    assert nchangesD(5) == 2
    assert nchangesD(6) == 2
    assert nchangesD(10) == 4
    assert nchangesD(15) == 6
