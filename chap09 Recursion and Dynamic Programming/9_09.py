"""
Write an algorithm to print all ways of arranging eight queens on
an 8x8 chess board so that none of them share the same row, column or
diagonal. In this case, "diagonal" means all diagonals, not just the
two that bisect the board.

- classic. Firstly, the queens should be on different rows and
columns. That is, for every row or column,there is one queen
exactly. Thus from the point of row, the queen just have the freedom
of column. Then for-loop or recursion can be applied to find all
possible arrangement.
"""

def eightqueen(n):
    if n == 1:
        return [[i] for i in range(1, 9)]
    
    arrangements = []
    for subarr in eightqueen(n - 1):
        for c in range(1, 9): # check all possible columns
            if c in subarr: # column occupied
                continue
            for qr, qc in enumerate(subarr):
                if abs(c - qc) == abs(n - qr - 1):
                    break
            else: # not on same column and diagonal, Python's special 'for-else' clause
                arrangements.append(subarr + [c])
    return arrangements


def test_eightqueen():
    assert len(eightqueen(8)) == 92

