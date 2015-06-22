"""
Describe an algorithm to find the smallest one million numbers in
one billion numbers. Assume that the computer memory can hold all one
billion numbers.

Obviously, the large scale of data is set to prevent you from sorting
the numbers.

If we could find a number, which has one million number smaller than
it, then problem is done. The number could be found by combinations of
statistics and estimation.

Scan the numbers to find min and max of the numbers. Divide the range
into bins. Scan the numbers again to get the freq within each
bin. Thus the number we desire could be estimated roughly. The above
steps could be run repeatedly to get an accurate result.

OR

Min heap. Store one million numbers into a heap with largest element
at the top. Then traverse the list. For each element, insert it into
the heap and delete the largest one (the top).

OR

Selection Rank Algorithm. (like quick sort).

"""

# TODO
