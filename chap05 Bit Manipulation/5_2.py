"""
Given a real number between 0 and 1 (e.g., 0.72) that is passed in
as a double, print the binary representation. If the number cannot be
represented accurately in binary with at most 32 characters, print
"ERROR".

- times by 2 and print the integral part.
"""

def binary(n):
    """
    get binary representation of a real number between 0 and 1
    """
    l = []
    cnt = 0
    while cnt < 32:
        if n == 0:
            break

        n *= 2
        if n >= 1:
            l.append('1')
            n -= 1
        else:
            l.append('0')
        cnt += 1

    if n == 0:
        return ''.join(l)
    else:
        return 'ERROR'


def test_binary():
    assert binary(0.5) == '1'
    assert binary(0.75) == '11'
    assert binary(0.3) == 'ERROR'
