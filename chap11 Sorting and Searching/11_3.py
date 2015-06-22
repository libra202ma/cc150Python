"""
Given a sorted array of n integers that has been rotated an
unknown number of times, write code to find an element in the
array. You may assume that the array was originally sorted in
increasing order.

EXAMPLE
Input: find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
Output: 8 (the index of 5 in the array)

- binary search. 
"""

def searchHelper(arr, target, left, right):
    print arr[left:right+1]
    mid = (left + right) / 2
    if arr[mid] == target:
        return mid
    if left > right:
        return -1

    if arr[left] < arr[mid]: # left half is sorted
        if arr[left] <= target <= arr[mid]:
            return searchHelper(arr, target, left, mid)
        else:
            return searchHelper(arr, target, mid + 1, right)
    elif arr[left] > arr[mid]: # right half is sorted
        if arr[mid] <= target <= arr[right]:
            return searchHelper(arr, target, mid, right)
        else:
            return searchHelper(arr, target, left, mid - 1)
    else: # left half are all repeats
        if arr[mid] != arr[right]:
            return searchHelper(arr, target, mid + 1, right)
        else:
            ret = search(arr, target, left, mid)
            if ret == -1:
                search(arr, target, mid + 1, right)
            else:
                return ret

    return -1


def search(arr, target):
    return searchHelper(arr, target, 0, len(arr) - 1)


def test_search():
    # assert search([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5) == 8
    assert search([10, 15, 20, 0, 5], 5) == 4
