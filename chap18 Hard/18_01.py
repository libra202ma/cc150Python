"""
Write a function that adds two numbers. You should not use + or
any arithmetic operators.

Notice XOR is addition without carry.

Assume two binary numbers, a and b. Then a + b = (a & b) << 1 + (a ^
b). Notice there is a recursion here. The recursion will exit when (a
& b) << 1 is 0.
"""


def add2(a, b):
    if a == 0:
        return b
    partial = a ^ b
    carry = (a & b) << 1
    return add2(carry, partial)


def test_add2():
    assert add2(0, 1) == 1
    assert add2(1, 1) == 2
    assert add2(7, 3) == 10
    assert add2(103, 251) == 354
