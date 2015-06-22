"""
Write a method to sort an array of string so that all the anagrams
are next to each other.

- sort characters of string to see if it is anagram to another
  string. If the two strings are anagrams, then define them as equal,
  this severs as the modified comparision func in the following main
  sort body. To keep the sort process stable, compare result of other
  string should also be modified. That is, the comparison function is
  actually compare list after sort.
- quicksort / mergesort the string array.

- Or use hashtable to group anagrams. The key should be sorted string
characters.
"""

def comparewithanagram(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    i = 0
    while i < len(s1) and i < len(s2):
        if s1[i] == s2[i]:
            i += 1
            continue
        else:
            return ord(s1[i]) - ord(s2[i])

    if i == len(s1) and i == len(s2):
        return 0
    elif i == len(s1):  # s2 is longer than s1
        return 0 - ord(s2[i])
    else:  # s1 is longer than s2
        return ord(s1[i])


def sortwithanagram(l):
    l.sort(cmp=comparewithanagram)


def test_sortwithanagram():
    l = ['world', 'test', 'hello', 'etts']
    sortwithanagram(l)
    assert l == ['world', 'hello', 'test', 'etts']
