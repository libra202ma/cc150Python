"""
There are three ants on different verticices of a triangle. What
is the probability of collision (between two or all of them) if they
start walking on the sides of the triangle? Assume that each ant
randomly picks a direction, with either direction being equally likely
to be chosen, and that they at the same speed.

Similarly, find the probablity of collision with n ants on an n-vertex
polygon.

- The ants will not collide if they choose a rotation direction. Thus
  the probablity they will collide is 1 - (0.5^3 * 2) = 3/4. For
  n-vertex polygon it is 1 - 2 * (1/2) ^ n = 1 - 1/2^(n-1)
"""
