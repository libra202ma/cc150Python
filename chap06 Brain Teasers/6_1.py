"""
You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but
one has pills of weight 1.1 grams. Given a scale that provides an
exact measurement, how would find the heavy bottle? YOU can only use
the scale once.

- Pick n pills from n-th bottles. Use the scale to get the total grams
Total. Then the heavier bottle is numbered by (TOTAL - 1 - 2 - 3 -
... - 20) * 10.
"""
