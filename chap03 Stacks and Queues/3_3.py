"""
Imagine a (literal) stack of plates. If the stack gets too high,
it might topple. Therefore, in real life, we would likely start a new
stack when the previous stack exceeds some threshold. Implement a data
structure SetOfStacks that mimics this. SetOfStacks should be composed
of several stacks and should create a new stack once the previous one
exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should
behave identically to a single stack (that is, pop() should return
the same value as it would if there where just a single stack).

- naive. use variables/lists to log all stack and current active stack.

FOLLOWUP

Implement a function popAt(int index) which performs a pop operation
on a specific sub-stack.

- same as above.
"""

class Stack():
    def __init__(self):
        self.arrlen = 10
        self.data = []
        self.narrs = 0
        self.addarr()
        self.top = -1

    def addarr(self):
        self.data.append([-1] * self.arrlen)
        self.narrs += 1

    def push(self, data):
        if self.top == self.arrlen - 1:
            self.addarr()
            self.top = 0
        else:
            self.top += 1
        self.data[self.narrs-1][self.top] = data

    def pop(self):
        res = self.data[self.narrs-1][self.top]
        if self.top == 0:
            self.data.pop()  # remove the last empty stack
            self.narrs -= 1
            self.top = self.arrlen - 1
        else:
            self.top -= 1
        return res

    def peek(self):
        return self.data[self.narrs-1][self.top]


def test_stack():
    s = Stack()
    for i in range(15):
        s.push(i)

    assert s.peek() == 14

    for i in range(5):
        s.pop()
    assert s.peek() == 9

    for i in range(10):
        s.pop()
    s.push(1)
    assert s.pop() == 1
