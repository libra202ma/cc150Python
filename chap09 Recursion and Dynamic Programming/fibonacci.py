def fibonacci_recursion(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci_recursion(n - 2) + fibonacci_recursion(n - 1)


def test_fibonacci_recursion():
    assert fibonacci_recursion(2) == 1
    assert fibonacci_recursion(5) == 5


fibonacci_nums = {0: 0, 1: 1}

def fibonacci_dp(n):
    """
    find n-th Fibonacci number using Dynamic Programming technique
    """
    if n <= 1:
        return fibonacci_nums[n]
    else:
        num = fibonacci_dp(n - 2) + fibonacci_dp(n - 1)
        fibonacci_nums[n] = num
        return num


def test_fibonacci_dp():
    assert fibonacci_dp(2) == 1
    assert fibonacci_dp(5) == 5
