"""
Imagine a robot sitting on the upper left corner of an X by Y
grid. The robot can only move in two directions: right and down. How
many possible paths are there for the robot to go from (0, 0) to (X,
Y)?

FOLLOW UP

Imagine certain spots are "off limits", such that the robot cannot
step on them. Design an algorithm to find a path for the robot from
the top left to the bottom right.

- recursion
- C_(X + Y)^X = (X + Y)! / (X! * Y!)

FOLLOW UP
- recursive. Careful though, not so easy.
"""

def findPath(x, y, path=[]):
    if x == 0 and y == 0:
        print path
        return True

    success = False
    if x >= 1 and isFree(x - 1, y):
        success = findPath(x - 1, y, path)
    if not success and y >= 1 and isFree(x, y - 1):
        success = findPath(x, y - 1, path)
    if success:
        path.append((x, y))
        return True
    else:
        return False
