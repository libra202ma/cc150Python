"""
A child is running up a staircase with n steps, and can hop either
1 step, 2 steps, or 3 steps at a time. Implement a method to count how
many possible ways the child can run up the stairs.

- same as representing n cents using coins.
- whoops, not really. The sequence of hops matters. On the last hop,
up to the n-th step, the child could have done either a single,
double, or triple step hop. And dynamic programming can be used to
reduce subfunction calls.
"""


def countways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return countways(n - 1) + countways(n - 2) + countways(n - 3)

def test_countways():
    assert countways(1) == 1
    assert countways(2) == 2
    assert countways(3) == 4

def countwaysDP(n, maps={}):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in maps:
        return maps[n]
    else:
        maps[n] = countways(n - 1, maps) + countways(n - 2, maps) + countways(n - 3, maps)
        return maps[n]


def test_countwaysDP():
    assert countways(1) == 1
    assert countways(3) == 4
