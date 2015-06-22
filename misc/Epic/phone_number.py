"""
Given number of digits of a phone number and number of disallowed
digits as input, find all permutations of numbers which do not have
two adjacent numbers the same, i.e. 1232 is allowed but not
1223. Disallowed digits can be upto 3, and can be included along with
the phone number. Also the phone number should start with 4 if it
contains the number 4.
"""


def numGen(numLen, disallowedDigits):
    nums = [[]]
    for i in range(numLen):
        nums2 = []  # list of numbers with one more digits
        for d in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if d in disallowedDigits:
                continue
            for n in nums:
                if n != [] and n[0] != 4 and d == 4:  # 4
                    continue
                if n != [] and d == n[-1]:  # adjacent numbers
                    continue
                # append one more digits
                n2 = n.copy()
                n2.append(d)
                nums2.append(n2)
        nums = nums2
    # convert to number
    for (i, n) in enumerate(nums):
        numStr = []
        for d in n:
            numStr.append(str(d))
        nums[i] = int(''.join(numStr))
    return nums


def test_numGen():
    print(numGen(4, [2, 5, 9]))
