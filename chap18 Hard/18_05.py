"""
You have a large text file containing words. Given any two words,
find the shortest distance (in terms of number of words) between them
in the file. If the operation will be repeated many times for the same
file (but different pairs of words), can you optimize your solution?

One time shot is easy to go.

Solution for multiple times.

For every word, scan the file and record the locations of the word
into an array.

To find the nearest distance, a slightly modified binary search could
be used. Cut the two array into same size. Find the location
differences at head and tail, if the location differences are with
different sign, it means the nearest location (moving toward to 0)is
within this range. Check the location difference at middle, then
decide whether to move on with left or right half.
"""

# TODO
