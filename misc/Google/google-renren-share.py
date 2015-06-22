"""
<http://blog.renren.com/share/250204113/17545076824?from=0101010202&ref=hotnewsfeed&sfet=102&fin=44&fid=25611594741&ff_id=250204113&platform=0&expose_time=1407861386>

## Phone Interview

Q: Talk about favourite programming languages and the reasons to
choose them. Any suggestions to improve the languages.

Q: Given a graph containing n vertex, how many edges could be added
to the graph without add cycles?

A: (n - 1)

Q: If it is a graph with directions, then how many edges could be
added without creating cycles?

A: n * (n - 1) / 2. Imagine the vertices are fitted into an array. For
every node, edges are added to all its following nodes.

Q: Given an array, the length of which is unknown, and the following
methods,

    string getWord(int index) {...}

Implement the following method,

    int getIndex(string word)

What is known about the array,

a. indices are sequencial, 0, 1, 2, ..., without absences.
b. all words are sorted alphabetically.
c. if the index is larger than the length of the array, getWord return
NULL. Similarly, getIndex should return NULL when the word is not
found.

A: single sided binary search + binary search

## Onsite Interview

### 0

Q: How to generate random positions in a square?

A: Just call a random number generator twice.

Q: How to get value of π through random simulation process?

A: Generate N random numbers in a square with edges equal to 1. Count
the number of the dots within the inscribed cycle, say it is n. Then π
is estimated at n/N.

Q: Write a function to generate π. Subsequent calling of this function
returns better precision.

A: The above function could be modified to satisfy the
requirement. The point is to keep data after the function returns. One
possible solution is to use static variables to hold the generated
random numbers. Or, closure could be used to capsule data within
function.

### 1

Q: Input a string, return all its fixed-point permutations.

- Fixed-point: If f(v) = v, then v is one of f's fixed-point.

A: TODO

### 2

Q: Box sorting. You have numbers from 1 to n, and they are randomly
put into boxes labeled at 1 to n. And you have another empty box
labeled at n + 1. You have only two access methods,

- get(int p), returns the content of box p
- move(int p, int q) - put the content of box p into box q

Write function to move numbers into the right boxes with least number
of operations.

A: TODO. 贪心算法?

### 3

Q:For an NxN matrix, implement the following methods,

- setValue(int x, int y, int v), set the value of cell (x, y) to v
- getSum(int x0, int x1, int y0, int y1)l, return the sum of cells (x0~x1, y0~y1)

Require best speed.

A: TODO. Dynamic programming.

### 4

Q: How to verify if a string is a valid unicode string?

A: TODO

Q: For an mxn chess board, put numbers of 1~m*n randomly on the board
cells, find the longest continuous incremental sequence. The sequence
is continuous means the next item located either upward, downward,
left, or right side of current item. For example, the longest
continuous incremental sequence is 1, 2, 3, 4

    8 5 9
    2 3 4
    1 6 7

A: TODO
"""
