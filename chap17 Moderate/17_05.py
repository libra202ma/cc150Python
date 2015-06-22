"""
The Game of Master Mind is played as follows:

The computer has four slots, and each slot will contain a ball that is
red (R), yellow (Y), green (G) or blue (B). For example, the computer
might have RGGB (Slot #1 is red, Slot #2 and #3 are green, Slot #4 is
blue).

You , the user, are trying to guess the solution. You might, for
example, guess YRGB.

When you guess the correct color for the correct slot, you get a
"hit". If you guess a color that exists but is in the wrong slot, you
get a "pseudo-hit". Note that a slot that is a hit can never count as
a pseudo-hit.

For example, if the actual solution is RGBY and you guess GGRR, you
have one hit and one pseudo-hit.

Write a method that, given a guess and a solution, returns the number
of hits and pseudo-hits.

"""

def cnt(actual, guess):
    hitCnt = 0
    phitCnt = 0
    for i in range(4):
        if actual[i] == guess[i]:
            hitCnt += 1
            actual[i] = 'X'
            guess[i] = 'X'

    for g in guess:
        if g != 'X' and g in actual:
            phitCnt += 1
            actual.remove(g)

    print(actual, guess)

    return (hitCnt, phitCnt)


def test_cnt():
    assert cnt(list('RGBY'), list('GGRR')) == (1, 1)
