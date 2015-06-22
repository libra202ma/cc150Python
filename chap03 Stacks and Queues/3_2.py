"""
How would you design a stack which, in addition to push and pop,
also has a function min which returns the minimum element? Push, pop
an min should all operate in O(1) time.


- append a local minimum attribute to every node. We use a global
  variable min, it is updated every time push operation happends. To
  get mininum of the stack, just peek the top element and extract its
  local min variable.

- Use a separate stack to keep track all mins. For push operation, we
  check if it is smaller than the top of mins stack, if it is, then
  push data into mins stack as well as the original stack. For every
  pop operation, check if the top of min is the same as the data to be
  poped, if it is, pop the data from the original stack and pop from
  the mins stack. To get the minimum, just peek the mins stack. This
  approach will help save memory usage, but problems happends when
  mutliple nodes have same data.
"""

class Item():
    def __init__(self, data, curmin):
        self.data = data
        self.curmin = curmin

class Stack():
    def __init__(self):
        self.data = []
        self.curmin = float('inf')

    def push(self, data):
        if data < self.curmin:
            self.curmin = data
        self.data.append(Item(data, self.curmin))

    def pop(self):
        return self.data.pop().data

    def min(self):
        return self.data[-1].curmin


def test_stack():
    s = Stack()
    s.push(2)
    s.push(1)
    s.push(3)
    assert s.min() == 1
    assert s.pop() == 3
    assert s.pop() == 1
    assert s.min() == 2
