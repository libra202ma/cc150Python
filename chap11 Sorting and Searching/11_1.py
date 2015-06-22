"""
You are given two sorted array, A and B, where A has a large
enough buffer at the end to hold B. Write a method to merge B into A
in sorted order.

- Merge sort. Work from back to front, i.e., copy larger cells of A or
B to the tail of A.
"""

def merge(A, B):
    i = len(A) - 1
    while A[i] == 0:
        i -= 1
    # now i point to last non-empty item of A
    j = len(B) - 1
    p = len(A) - 1
    while i < p:
        if A[i] > B[j]:
            A[p] = A[i]
            p -= 1
            i -= 1
        else:
            A[p] = B[j]
            p -= 1
            j -= 1


def test_merge():
    A = [1, 2, 6, 7, 0, 0, 0]
    B = [3, 4, 5]
    merge(A, B)
    assert A == [1, 2, 3, 4, 5, 6, 7]
