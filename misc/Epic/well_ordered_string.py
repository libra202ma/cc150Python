def cntWellOrderedString(nCharsLeft, lastChar=''):
    if nCharsLeft == 0:
        return 1

    if lastChar == '':
        charStart = ord('a')
    else:
        charStart = ord(lastChar) + 1

    cnt = 0
    for c in range(charStart, ord('z') + 1):
        c = chr(c)
        cnt += cntWellOrderedString(nCharsLeft - 1, c)

    return cnt


def test_cntWellOrderedString():
    assert cntWellOrderedString(2) == 325
