"""
A monochrome screen is stored as a single array of bytes, allowing
eight consecutive pixels to be stored in one byte. The screen has
width w, where w is divisible by 8 (that is, no byte will be split
across rows). The height of the screen, of course, can be derived from
the length of the array and the width. Implement a function
drawHorizontalLine(byte[] screen, int width, int x1, int x2, int y)
which draws a horizontal line from (x1, y) to (x2, y).

- naive. the bits start from y * w + x1 to y * w + x2, set those bits
  to 1.
- to improve, set the full bytes at once.
"""

def drawHorizontalLine(screen, width, x1, x2, y):
    bitstart = y * width + x1
    bitend = y * width + x2
    for byteidx in range(bitstart/8 + 1, bitend/8):
        screen[byteidx] = 0xFF

    # deal with the start byte and end byte
    screen[bitstart/8] |= 2 ** ((bitstart / 8 + 1) * 8 - bitstart) - 1
    screen[bitend/8] |= (2 ** (bitend - bitend / 8 * 8) - 1) << ((bitend / 8 + 1) * 8 - bitend)


def test_drawHorizontalLine():
    screen = [0x00, 0x00, 0x00, 0x00]
    result = [0x0F, 0xFF, 0xFF, 0xF0]
    drawHorizontalLine(screen, 1280, 4, 4 + 3 * 8, 0)
    assert screen == result
    screen = [0x00, 0x00, 0x00, 0x00]
    result = [0x00, 0xFF, 0xFF, 0x00]
    drawHorizontalLine(screen, 1280, 8, 8 + 8 * 2, 0)
    assert screen == result
