"""
Implement the function,

// if there is two numbers in the nums array that are sum to target, return
// true, else return false.
bool sumToTarget(int[] nums, int target);

"""


def sumToTarget_BT1(nums, target):
    """
    Brute Force.

    For every number ni, check all the following items nj, if ni + nj
    == target, return true. Works at O(n^2).
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False


def test_sumToTarget_BT1():
    assert sumToTarget_BT1([1, 3, 9, 1], 4) is True
    assert sumToTarget_BT1([1, 3, 9, 1], 6) is False


def sumToTarget_BT2(nums, target):
    """
    Brute Force 2.

    For every number ni, check all the following items nj, if nj ==
    target - ni, return true. Works at O(n^2).
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return True
    return False


def test_sumToTarget_BT2():
    assert sumToTarget_BT2([1, 3, 9, 1], 4) is True
    assert sumToTarget_BT2([1, 3, 9, 1], 6) is False


def binarySearch(nums, left, right, target):
    if left > right:
        return False

    mid = (left + right) // 2
    if nums[mid] == target:
        return True
    elif nums[mid] < target:
        return binarySearch(nums, mid + 1, right, target)
    else:
        return binarySearch(nums, left, mid - 1, target)


def test_binarySearch():
    assert binarySearch([1, 3, 9], 0, 2, 3) is True
    assert binarySearch([1, 3, 9], 0, 2, 1) is True
    assert binarySearch([1, 3, 9], 0, 2, 2) is False


def sumToTarget_BS(nums, target):
    """
    Binary Search.

    Based on Brute Force 2. Sort the array first. For every number ni,
    search the following for (target - ni). Since the array is sorted,
    the search process works at O(logn). Thus the whole algorithm
    works at O(nlogn).
    """
    nums = sorted(nums)
    for i in range(len(nums)):
        return binarySearch(nums, i + 1, len(nums) - 1, target - nums[i])


def test_sumToTarget_BS():
    assert sumToTarget_BS([1, 3, 9, 1], 4) is True
    assert sumToTarget_BS([1, 3, 9, 1], 6) is False


def sumToTarget_DP(nums, target):
    """
    Dynamic Programming / Cache.

    Based on previous Binary Search version. Create a cache for
    visited items using HashMap. For every item ni, search (target -
    ni) in the cache. If found, return true, else put ni in the
    cache. Since the search process works at O(logn), the overall
    algorithm works at O(nlogn).
    """
    cache = {}
    for n in nums:
        if (target - n) in cache:
            return True
        else:
            cache[n] = True
    return False


def test_sumToTarget_DP():
    assert sumToTarget_DP([1, 3, 9, 1], 4) is True
    assert sumToTarget_DP([1, 3, 9, 1], 6) is False


"""
NOTE

For languages other than Python, there might be overflow exception in
the later 3 implementations. Consider target is close to Integer.MIN
and ni is a big int, overflow happens. To solve this problem, just put
the if statement inside a try block, catch Overflow exceptions and do
nothing, cause if overflow happens, i.e., (target - ni) could not fit
into int type, it could not be in the nums array, which is of type
int, and we do not need to put ni in cache, since (target - ni) could
not be in the array thus ni will never be used.
"""
