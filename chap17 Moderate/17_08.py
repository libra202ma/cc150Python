"""
You are given an array of integers (both positive and
negative). Find the contiguous sequence with the largest sum. Return
the sum.

EXAMPLE
Input: 2, -8, 3, -2, 4, -10
Output: 5 (i.e., (3, -2, 4))

Dynamic Programming.

Keep track of all active lists (an active list means the list continue
until item i - 1). For the item i, if it is a positive number, then
add it to all active lists, cause the sum will be larger; further, if
i - 1 is negative, then this item i could be serve as the starting
point as a new active list. If item i is negative, find the largest
sum in active lists, meaning the lists could possibly ended before
this item; meanwhile, add item i to all active lists, in case there is
a larger positive number following at i + 1.

The algorithm works at O(n).
"""

def largestSum(l):
    deadlists = []
    # basic case
    activelists = [[l[0]]]
    if l[0] >= 0:
        prevsign = False
    else:
        prevsign = True

    for n in l[1:]:
        if n >= 0:
            for al in activelists:
                al.append(n)
            # If the previous number is negative, this positive number
            # could serve as a start of a new contiguous sequence
            if prevsign is False:
                activelists.append([n])
            prevsign = True
        else:
            for al in activelists:
                # copy the active lists to dead lists, i.e., end the
                # activelists lists
                deadlists.append(al.copy())
                # Append current number to active lists, in case there
                # is a larger positive number following
                al.append(n)
            prevsign = False

    deadlists += activelists
    print(deadlists)
    return max([sum(dl) for dl in deadlists])


def test_largestSum():
    assert largestSum([2, -8, 3, -2, 4, -10]) == 5
    assert largestSum([-2, -4]) == -2
