"""

"""



def searchHelper(arr, left, right, target):
    mid = (left + right) / 2
    if arr[mid] == target:
        return mid
    if left > target:
        return -1

    if arr[mid] < target:
        return searchHelper(arr, mid + 1, right, target)
    else:
        return searchHelper(arr, left, mid, target)

def search(arr, target):
    return searchHelper(arr, 0, len(arr) - 1, target)


def test_search():
    assert search([1], 1) == 0
    assert search([1, 2], 2) == 1
