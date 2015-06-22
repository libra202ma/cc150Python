# Kadane's algorithm
def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def test_max_subarray():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def max_subarrayNonzero(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# Because of the way this algorithm uses optimal substructures (the
# maximum subarray ending at each position is calculated in a simple
# way from a related but smaller and overlapping subproblem: the
# maximum subarray ending at the previous position) this algorithm can
# be viewed as a simple example of dynamic programming.
