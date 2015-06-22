"""
The cows and bulls game, Player A chooses a word and player B guesses a word. You say bulls when a character in the player B's guess match with a character in player A's word and also it is in the corect position as in A's word. You say cows, when a character in the player B's word match the character in player A, but it is not in the correct position. The characters are case insensitive. Given two words player A's and player B's,Write a function that return the number of bulls and no of cows. For example,
A - Picture B- Epic, bulls -0, cows - 4
A - forum B - four, bulls - 3 cows - 1
"""


def bulls_and_cows(word, guess):
    word = list(word.lower())
    guess = list(guess.lower())

    # check for bulls
    nbulls = 0
    ncows = 0
    for i in range(min(len(word), len(guess))):
        if guess[i] == word[i]:
            nbulls += 1
        elif guess[i] in word:
            ncows += 1

    return (nbulls, ncows)


def test_bulls_and_cows():
    assert bulls_and_cows('Picture', 'Epic') == (0, 4)
    assert bulls_and_cows('forum', 'four') == (2, 2)
