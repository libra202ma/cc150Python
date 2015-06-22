"""
In the classic problem of the Towers of Hano, you have 3 towers
and N disks of different sizes which can be slide onto any tower. The
puzzle starts with disks sorted in ascending order of size from top to
bottom (i.e., each disk sits on top of an even larger one). You have
the following constraints:

(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto the next tower.
(3) A disk can only be placed on top of a larger disk.

Write a program to move the disks from the first tower to the last
using stacks.

- recursion. classic problem.
"""

def solve_Hanoi(s1, s2, s3, n):
    if n <=0:
        return

    solve_Hanoi(s1, s3, s2, n - 1)
    var = s1.pop()
    s3.append(var)
    solve_Hanoi(s2, s1, s3, n - 1)



def test_solve_Hanoi():
    s1 = [5, 4, 3, 2, 1]
    s2 = []
    s3 = []
    solve_Hanoi(s1, s2, s3, len(s1))
    assert s1 == []
    assert s2 == []
    assert s3 == [5, 4, 3, 2, 1]
