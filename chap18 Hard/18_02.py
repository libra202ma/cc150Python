"""
Write a method to shuffle a deck of cards. It must be a prefect
shuffle - in other words, each of the 52! permutations of the deck has
to be equally likely. Assume that you are given a random generator
which is perfect.

Keep an list of numbers, from 0 to 51. Generate a random number n1,
which is between 0 to 51, assign the number with index n1 to the first
card, and delete this number in the array (now the size of the array
is 51). Then generate another random number n2 between 0 to 50, assign
the number with index n2 to the second card, and delete the number
(notice the number may not equal to its index now). So on so forth.

(There are alternatives approaches if we do not want the change size
of the number array. Instead of delete the number, we simply mark the
this number has already been taken out. In the following round, always
generate a random number between 0 and 51, if the number with the
index has been crossed out, generate another random number until the
number is fresh new.)

With this approach, the possibility of each number chosen by each card
is equal. This ensures each permutation to be equally likely.

See the reference answer, it is more cleaner.
"""

# TODO
