"""
Implement a MyQueue class which implements a queue using two
stacks.

- Naive. For every enqueue operation, just enqueue it onto s1. For
  every dequeue operation, we first pop all nodes from s1 to s2, then
  pop from s2 to get the oldest element, then pop all nodes from s2
  back to s1.
- lasy execuation. Again for enqueue operation, we push it onto
  s1. But exec dequeue from s2. If s2 is empty, poping all nodes from
  s1 to s2. If s2 is not empty, the top of s2 is oldest one, just pop
  it. (WOW)
"""


class MyQueue:
    def __init__(self):
        self.newstack = []
        self.oldstack = []

    def push(self, data):
        self.newstack.append(data)

    def pop(self):
        if self.oldstack:
            return self.oldstack.pop()
        elif self.newstack:
            # dump newstack to oldstack
            while self.newstack:
                self.oldstack.append(self.newstack.pop())
            return self.oldstack.pop()
        else:
            return None


def test_myqueue():
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.pop() == None
