"""
Design an algorithm to find the k-th number such that the only
prime factors are 3, 5, 7.


*******
- P = 3^i0 * 5^i1 * 7^i2

Ak = min({3, 5, 7} X {A1, A2, A3, ... Ak-1})
"""


def findprime(k):
    q3 = []
    q5 = []
    q7 = []

    magic = [1]
    q3.append(3 * 1)
    q5.append(5 * 1)
    q7.append(7 * 1)

    for i in range(k):
        q3min = q3[0]
        q5min = q5[0]
        q7min = q7[0]
        minimum = min(q3min, q5min, q7min)
        magic.append(minimum)
        if minimum == q3min:
            q3.remove(minimum)
            q3.append(3 * minimum)
            q5.append(5 * minimum)
            q7.append(7 * minimum)
        elif minimum == q5min:
            q5.remove(minimum)
            q5.append(5 * minimum)
            q7.append(7 * minimum)
        else:
            q7.remove(minimum)
            q7.append(7 * minimum)

    return magic[-1]


def test_findprime():
    assert findprime(1) == 3
    assert findprime(6) == 21

    for k in range(15):
        print findprime(k)
