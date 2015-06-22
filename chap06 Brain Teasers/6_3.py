"""
You have a five-quart jug, a three-quart jug, and an unlimited
supply of water (but no measuring cups). How would you come up with
exactly four quarts of water? Note that the jugs are oddly shaped,
such that filling up exactly "half" of the jug would be impossible.


| action                        | 5 quarts | 3 quarts |
|-------------------------------+----------+----------|
| fill into 5                   |        5 |        0 |
| fill into 3 using 5's content |        2 |        3 |
| dump 3                        |        2 |        0 |
| transfer from 5 to 3          |        0 |        2 |
| fill into 5                   |        5 |        2 |
| fill into 3 using 5           |        4 |        3 |

"""
