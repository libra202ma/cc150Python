def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mididx = len(arr)/2;
    left = mergesort(arr[:mididx])
    right = mergesort(arr[mididx:])
    i = 0 # left half index
    j = 0 # right half index
    arr = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    # append left parts
    # onely one of the following two lines will make real effect since
    # one of i, j must reach the end of the array after finish the
    # above loop
    arr += left[i:]
    arr += right[j:]
    return arr
        

def test_mergesort():
    assert mergesort([54, 26, 93, 17, 77, 31, 44, 55, 20]) == [17, 20, 26, 31, 44, 54, 55, 77, 93]
