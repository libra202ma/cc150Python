from math import sqrt


def getPrimes(n):
    # get all primes smaller than n
    nums = [1 for i in range(n)]  # 0...n-1
    nums[0] = 0  # 0 is not prime
    nums[1] = 0  # 1 is not prime
    for d in range(2, int(sqrt(n)) + 1):
        i = 2 * d
        while i < n:
            nums[i] = 0
            i += d
    return [i for (i, n) in enumerate(nums) if n == 1]


def test_getPrimes():
    assert getPrimes(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def Goldbach(n):
    if n % 2 != 0:
        return -1

    primes = getPrimes(n)
    visited = set()
    for p in primes:
        if n - p in visited:
            return (n - p, p)
        else:
            visited.add(p)


def test_Goldbach():
    assert Goldbach(11) == -1
    assert Goldbach(34) == [11, 23]
