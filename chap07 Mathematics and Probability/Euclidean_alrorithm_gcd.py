"""
The main principle is that GCD does not change if the smaller
number is subtracted from the larger number.

"""


def gcd(a, b):
    """
    assume a >= b
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def test_gcd():
    assert gcd(252, 105) == 21
    assert gcd(3, 7) == 1
