"""
Describe how you could use a single array to implement three
stacks.

- naive. stacks start 0, 1, 2, respectively, with step size of 3. Or
stacks start from 0, 1/3, 2/3 with time step of 1.
"""


class Stack3():
    def __init__(self):
        self.arr = [0] * 30
        self.tops = [-3, -2, -1]

    def push(self, data, i):
        """Push data to i-th stack"""
        self.tops[i] += 3
        self.arr[self.tops[i]] = data

    def pop(self, i):
        """Pop data from i-th stack"""
        self.tops[i] -= 3
        return self.arr[self.tops[i] + 3]




def test():
    s = Stack3()
    s.push(0, 0)
    s.push(1, 1)
    s.push(2, 2)
    assert s.arr[0:3] == [0, 1, 2]
    assert s.pop(1) == 1
