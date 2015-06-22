"""
There is an 8x8 chess board in which two diagonally opposite
corners have been cut off. You are given 31 dominos, and a single
domino can cover exactly two squares. Can you use the 31 dominos to
cover the entire board? Prove your answer (by providing an exaple or
showing why it's impossible).

- Impossible. The extra square will pop up and can not make one with
the other extra square in the last row.
- Color the squares alternatively using black and white. If two
opposite corners are cutted off, say there are 32 white and 30 black
left. For every domino, it takes up one black and one white. So we
cannot cover 32 white with 31 dominos.
"""
