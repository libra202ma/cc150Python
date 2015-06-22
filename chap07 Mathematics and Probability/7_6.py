"""
Given a two-dimensional graph with points on it, find a line which
passes the most number of points.

*******

- Brute force. Compute the lines for every two points, there should be
n(n-1)/2 lines. Use a hashtable to cache those lines. Then find the
most common one.
"""
