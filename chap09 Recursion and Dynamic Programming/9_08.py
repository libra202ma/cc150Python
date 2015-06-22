"""
Given an infinite number of quarters (25 cents), dimes (10 cents),
nickels (5 cents) and pennies (1 cent), write code to calculate the
number of ways of representing n cents.


- brute-force. Using for-loops to check if the sum of all possible
  combinations equals to n.
- recursion. The base case is that representing n cents using only 1
cents. Then ways of representing of n cents using 1 and 5 cents = ways
of using at least one 5 cents + ways of using only 1 cents to
represent left parts.

<http://www.cs.ucf.edu/~dmarino/ucf/cop3503/lectures/DynProgChange.doc>

- dynamic programming. The key point is that the number of ways to make change for n cents using denomination d can be split up into counting two groups:
1. the number of ways to make changes for n cents using denominations LESS than d
2. the number of ways to make changes for n cents using at least ONE
coin of denomination d.
"""

def countways(n, coins=[1, 5, 10, 25]):
    if coins == [1]:
        return 1

    nways = 0
    for i in range(n/coins[-1] + 1):
        nways += countways(n - i * coins[-1], coins[:-1])

    return nways


def test_countways():
    assert countways(1) == 1
    assert countways(5) == 2
    assert countways(6) == 2
    assert countways(10) == 4
    assert countways(15) == 6

# dynamic programming, bottom up
def countwaysDP(n):
    waystable = [[], [], [], []]
    denoms = [1, 5, 10, 25]
    for cents in range(1, n+1):
        for denomidx, denom in enumerate(denoms):
            if denom == 1:
                waystable[denomidx].append(1)
            elif cents - denom >= 0:
                waystable[denomidx].append(waystable[denomidx - 1][cents - 1] + waystable[denomidx][cents - 1 - denom])
            else:
                waystable[denomidx].append(waystable[denomidx - 1][cents - 1])

    return waystable[-1][-1]


def test_countwaysDP():
    assert countwaysDP(1) == 1
    assert countwaysDP(15) == 6


# dynamic programming, top down
def countwaysDP2(n, maps={}, coins = [1, 5, 10, 25]):
    # maps has keys (n, coin), which keep tracks of number of ways to
    # represent n cents using largest coins equals to coin
    if coins == [1]:
        return 1

    if (n, coins[-1]) in maps:
        return maps[(n, coins[-1])]

    nways = 0
    for i in range(n/coins[-1] + 1):
        nways += countwaysDP2(n - i * coins[-1], maps, coins[:-1])

    maps[(n, coins[-1])] = nways
    return nways


def test_countwaysDP2():
    assert countwaysDP2(15) == 6
