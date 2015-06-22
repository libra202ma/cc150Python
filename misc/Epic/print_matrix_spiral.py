def strSpiral(M):
    N = len(M)
    nlayers = N // 2

    for l in range(nlayers):
        # top border
        for j in range(N - 1 - l, l, -1):
            print(M[l][j], end='')
        # left border
        for i in range(l, N - 1 - l):
            print(M[i][l], end='')
        # bottom border
        for j in range(l, N - 1 - l):
            print(M[N - 1 - l][j], end='')
        # right border
        for i in range(N - 1 - l, l, -1):
            print(M[i][N - 1 - l], end='')

    # for odd number of layers, add the center one
    if N % 2 == 1:
        print(M[N//2][N//2])
    else:
        print()


def test_strSpiral():
    M = [[1, 2], [3, 4]]
    strSpiral(M)
    M = [[1]]
    strSpiral(M)
