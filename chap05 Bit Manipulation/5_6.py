"""
Write a program to swap odd and even bits in an integer with as
few instructions as possible. (e.g., bit 0 and bit 1 are swapped, bit
2 and bit 3 are swapped, and so on.)

- extract even bits and shift to right by 1 bit, extract odd bits and
shift to left by 1 bit, then merge the above two.
"""

def swapbits(n):
    # assume 32-bit integers
    evenbits = n & 0x55555555
    oddbits = n & 0xAAAAAAAA
    return (evenbits << 1) | (oddbits >> 1)


def test_swapbits():
    assert swapbits(0b1010) == 0b0101
    assert swapbits(0b10101010) == 0b01010101
