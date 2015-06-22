"""
There is a building of 100 floors. If an egg drops from the Nth
floor or above, it will break. If it's dropped from any floor below,
it will not break. You're given two eggs. Find N, while minimizing the
number of drops for the worst case.

- Use the egg1 as binary search (starting from 50, cause 100 will
definitely break the egg), if the egg ok, then search up, if it
breaks, then retrive the last step when it is ok. Start egg2 from this
point and moves up, when eggs breaks, then N is it.

NONO, if egg1 breaks at 50, egg2 will have 50 floors to check.

Drops(Egg 1) + Drops(Egg 2) must be always same.

So incremental of Egg 1 should decrease every time after a drop.

X + (X - 1) + (X - 2) + ... + 1 = 100

X = 14
"""
