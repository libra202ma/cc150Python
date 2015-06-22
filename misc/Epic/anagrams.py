def permutations(l):
    """
    Find all permutations of l.

    l is list of chars.
    """
    if len(l) == 1:
        return [l, ]

    partialPMList = permutations(l[:-1])
    pmList = []
    for partialPM in partialPMList:
        for i in range(0, len(l)):
            pm = partialPM.copy()
            pm.insert(i, l[-1])
            pmList.append(pm)

    return pmList


def test_permutations():
    assert permutations([1, 2, 3]) == \
        [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]



def anagrams(s):
    # find all lowercase characters
    loweridx = []
    lowerchars = []
    for (i, c) in enumerate(s):
        if c.islower():
            loweridx.append(i)
            lowerchars.append(c)

    # get all permutations
    pmList = permutations(lowerchars)
    #
    strList = list(s)
    anagramList = []
    for pm in pmList:
        anagram = strList.copy()
        for (i, c) in zip(loweridx, pm):
            anagram[i] = c
        anagramList.append(''.join(anagram))

    return anagramList


def test_anagrams():
    assert anagrams('Tcl') == ['Tlc', 'Tcl']
    assert anagrams('That') == ['Ttah', 'Tath', 'Taht', 'Ttha', 'Thta', 'That']
