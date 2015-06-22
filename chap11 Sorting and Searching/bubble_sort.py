"""
"""


def bubble_sort(arr):
    """
    O(n^2)
    """
    for i in range(len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def test_bubble_sort():
    assert bubble_sort([6, 9, 3, 2, 5]) == [2, 3, 5, 6, 9]
