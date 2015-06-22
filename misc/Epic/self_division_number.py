def getDigits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    digits.reverse()
    return digits


def test_getDigits():
    assert getDigits(128) == [1, 2, 8]


def isSDN(n):
    """
    Check if a number is Self Division Number.
    """
    digits = getDigits(n)

    if 0 in digits:
        return False

    for d in digits:
        if n % d != 0:
            return False
    return True


def test_isSDN():
    assert isSDN(128) is True
    assert isSDN(23) is False


def getAllSDN(n):
    SDN = []
    for i in range(10, n + 1):
        if isSDN(i):
            SDN.append(i)
    return SDN


def test_getALLSDN():
    assert getAllSDN(128) == [11, 12, 15, 22, 24, 33, 36, 44, 48, 55, 66, 77, 88, 99, 111, 112, 115, 122, 124, 126, 128]
