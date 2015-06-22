"""
"""


def selection_sort(arr):
    """
    O(n^2)
    """

    for i in range(len(arr)):
        minidx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minidx]:
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]

    return arr


def test_selection_sort():
    assert selection_sort([6, 9, 3, 2, 5]) == [2, 3, 5, 6, 9]
