from collections import deque

class Queue():
    def __init__(self):
        self.data = deque()

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        self.popleft()
