"""
The decimal and octal values of some numbers are both palindromes
sometimes. Find such numbers within a given range.
"""


def isPalindromeInDecimal(n):
    digits = list(str(n))
    if digits == digits[::-1]:
        return True
    else:
        return False


def test_isPalindromeInDecimal():
    assert isPalindromeInDecimal(12321) is True
    assert isPalindromeInDecimal(1232) is False


def isPalindromeInOctal(n):
    digits = list(oct(n))[2:]  # convert to octal string
    if digits == digits[::-1]:
        return True
    else:
        return False


def test_isPalindromInOctal():
    assert isPalindromeInOctal(0o12321) is True


def isPalindrome(n):
    if isPalindromeInDecimal(n) and isPalindromeInOctal(n):
        return True
    else:
        return False


def getAllPalindrome(start, end):
    palindromes = []
    for n in range(start, end):
        if isPalindrome(n):
            palindromes.append(n)

    return palindromes


def test_getAllPalindrome():
    print(getAllPalindrome(100, 1000))
