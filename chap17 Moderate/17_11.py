"""
Implement a method rand7() given rand5(). That is, given a method
that generates a random number between 0 and 4 (inclusive), write a
method that generate a random number between 0 and 6 (inclusive).

The idea is to have a rand10() first (using scales), then cut it to
get rand7().
"""

import random
random.seed(0)

def rand5():
    return random.randint(0, 4)


def test_rand5():
    freq = {}
    numExp = 50000
    for i in range(numExp):
        n = rand5()
        if n not in freq:
            freq[n] = 1
        else:
            freq[n] += 1
    assert (max(freq.values()) - min(freq.values())) / numExp < 0.01

def rand7():
    n = rand5()
    if n in [0, 1]:
        # 0..4 random
        return rand5()
    elif n in [2, 3]:
        # 5..6 random
        m = rand5()
        if m <= 1:
            return 5 + m
        else:
            return rand7()
    else:
        return rand7()


def test_rand7():
    freq = {}
    numExp = 70000
    for i in range(numExp):
        n = rand7()
        if n not in freq:
            freq[n] = 1
        else:
            freq[n] += 1
    print(freq)
    assert (max(freq.values()) - min(freq.values())) / numExp < 0.01
