class Stack():
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]
