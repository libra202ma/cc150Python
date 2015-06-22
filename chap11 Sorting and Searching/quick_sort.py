def quicksort(arr):
    if len(arr) <= 1:
        return

    pivot = arr[0]
    leftmark = 1
    rightmark = len(arr) - 1

    done = False
    while not done:
        while leftmark <= rightmark and arr[leftmark] <= pivot:
            # try to find one term larger than pivot
            leftmark += 1
        while leftmark <= rightmark and arr[rightmark] >= pivot:
            # try to find one term smaller than pivot
            rightmark -= 1
        if leftmark > rightmark:
            done = True
        else:
            arr[leftmark], arr[rightmark] = arr[rightmark], arr[leftmark]
    arr[0], arr[rightmark] = arr[rightmark], arr[0]
    quicksort(arr[:rightmark])
    quicksort(arr[rightmark+1:])


def test_quicksort():
    assert quicksort([54, 26, 93, 17, 77, 31, 44, 55, 20]) == [17, 20, 26, 31, 44, 54, 55, 77, 93]

