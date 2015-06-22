"""
An animal shelter holds only dogs and cats, and operates on a
strictly "first in, first out" basis. People must adopt either the
"oldest" (based on arrival time) of all animals at the shelter, or
they can select whether they would prefer a dog or a cat (and will
receive the oldest animal of that type). They cannot select which
specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue,
dequeueAny, dequeueDog, and dequeueCat. You may use the build-in
LinkedList data structure.

- naive. Use one queue. For dog/cat, just dequeue in the head. For dog
  or cat, use an extra stack to cache, dequeue in the head until a dog
  or cat is find, then enqueue back from the stack into the head.
- Use two queues, one for dog and another for cat. For enqueue
  operation, we add an extra attribute order as an timestamp. For
  [dog|cat] dequeue operation, first peek both dog and cat queues,
  compare them and return the oldest. For dog or cat dequeue
  operation, just dequeue from the corresponding queue.
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'stacks_and_queues'))

from stack import Stack

class Animal():
    def __init__(self, data, id):
        self.data = data
        self.id = id

class AnimalStack():
    def __init__(self):
        self.catstack = Stack()
        self.dogstack = Stack()
        self.id = 0  # id used as timestamp

    def push(self, data):
        self.id += 1
        if data is cat:
            self.catstack.push(Animal(data, self.id))
        else:
            self.dogstack.push(Animal(data, self.id))

    def pop(self):
        cat = self.catstack.peek()
        dog = self.catstack.peek()
        if cat.id < dog.id:
            return cat
        else:
            return dog

    def popcat(self):
        return self.catstack.pop()

    def popdog(self):
        return self.dogstack.pop()
