"""
Write a function to determine the number of bits required to
convert integer A to integer B.

EXAMPLE
Input: 31, 14
Output: 2

- Count how many 1s in XOR result
"""

def cntdiffbits(n1, n2):
    cnt = 0
    for b in bin(n1 ^ n2)[2:]:
        if b == '1':
            cnt += 1

    return cnt

def test_cntdiffbits():
    assert cntdiffbits(31, 14) == 2
