"""
Given a sorted array of strings which is interspersed with empty
strings, write a method to find the location of a given string.

EXAMPLE
Input:find "ball" in  {"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""}
Output: 4

- Binary search. Skip to closest non-empty string if found empty string.
"""


def searchHelper(l, start, end, target):

    if start > end:
        return None

    while not l[start]:  # find non-empty start
        start += 1
    while not l[end]:  # find non-empty end
        end -= 1
    mid = (start + end) / 2
    offset = 0
    while True:
        if 0 <= mid + offset < len(l) and l[mid + offset]:
            mid = mid + offset
            break
        elif 0 <= mid + offset < len(l) and l[mid - offset]:
            mid = mid - offset
            break
        offset += 1
    # now mid point to a non-empty item
    if l[mid] == target:
        return mid
    elif l[mid] < target:
        searchHelper(l, mid + 1, end, target)
    else:
        searchHelper(l, start, mid - 1, target)


def search(l, target):
    return searchHelper(l, 0, len(l) - 1, target)


def test_search():
    l = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    assert search(l, "ball") == 4
    assert search(l, "hello") == None
