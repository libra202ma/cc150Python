"""
Colorful Number

A number can be broken into different sub-sequence parts. Suppose, a
number 3245 can be broken into parts like 3 2 4 5 32 24 45 324
245. And this number is a colorful number, since product of every
digit of a sub-sequence are different are different. That is, 3 2 4 5
(3 * 2) = 6, (2 * 4) = 8, (4 * 5) = 20 (3 * 2 * 4) = 24 (2 * 4 * 5) =
40.

But 325 is not a colorful number as it generates 3 2 6 (3 * 2) = 6
(2 * 6) = 12. You have to write a function that tells if the given
number is a colorful number or not.
"""


def getDigits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    digits.reverse()
    return digits


def test_getDigits():
    assert getDigits(3245) == [3, 2, 4, 5]


def isColorful(n):
    digits = getDigits(n)
    # return early when there is 0 or 1 in the digits
    if (1 in digits) or (0 in digits):
        return False

    products = set()
    for sublen in range(1, len(digits)):
        for subidx in range(len(digits) - sublen + 1):
            p = 1
            for d in digits[subidx:subidx + sublen]:
                p *= d
            if p in products:
                return False
            else:
                products.add(p)

    return True


def test_isColorful():
    assert isColorful(3245) is True
    assert isColorful(326) is False
