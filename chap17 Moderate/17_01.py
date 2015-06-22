"""
Write a function to swap a number in place (that is, without
temporary variables).

Make use of immediate result.

Assume,

A = a
B = b

Step 1

B = A - B = a - b

Step 2

A = A - B = a - (a - b) = b

Step 3

B = A + B = b + (a - b) = a


There might exists other approaches, like using bit manipulation, but the
basic idea is same as this one.
"""


def swap(a, b):
    b = a - b
    a = a - b
    b = a + b
    return (a, b)


def test_swap():
    assert swap(3, 7) == (7, 3)
