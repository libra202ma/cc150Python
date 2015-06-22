"""
You have basketball hoop and someone says that you can play one of two games.

Game 1: You get one shot to make the hoop.

Game 2: You get three shots and you have to make two of three shots.

If p is the probability of making a perticular shot, for which values
of p should you pick one game or the other?

- Game 1: p
- Game 2: C_3^2 * p^2 * (1 - p) + p^3 = 3p^2 - 2p^3

If p < 0.5, choose Game 1. Otherwise choose Game 2.
"""
