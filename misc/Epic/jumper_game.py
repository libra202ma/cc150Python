"""
Jumper Game: A NxN grid which contains either of 0-empty, 1 -
player1, 2 - player 2. Given a position in the grid, find the longest
jump path. For jump path, you can horizontally or vertically, you can
jump on opponent cell and also the landing cell should be empty. No
opponent cell can be jumped more than once. Write a function which
takes grid and a specific position in the grid, and returns the
longest possible number of jumps in the grid.
"""

def longest_possible_jumps(grid, player, pos, path=[]):
    if grid[pos.x][pos.y] == 0:
        return 1

    maxlen = 1
    for nextpos in [(pos.x - 1, pos.y),
                    (pos.x, pos.y + 1),
                    (pos.x + 1, pos.y),
                    (pos.x, pos.y - 1)]:
        if grid[pos.x][pos.y] != player and grid[nextpos.x][nextpos.y] != player:
            continue
        if nextpos not in path:
            path2 = path.copy()
            path2.append(pos)
            maxlen = max(maxlen,
                         longest_possible_jumps(grid, nextpos, path2))

    return maxlen
