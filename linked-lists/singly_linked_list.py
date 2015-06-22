#!/usr/bin/env python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self, l=[]):
        self.n = 0
        self.head = Node(0) # dummy
        self.tail = Node(0) # dummy
        p = self.head
        for i in l:
            newnode = Node(i)
            p.next = newnode
            p = p.next
            self.n += 1
        p.next = self.tail

    def list(self):
        """
        return list as an array

        """
        l = []
        p = self.head.next # first real element
        while p != self.tail:
            l.append(p.data)
            p = p.next
        return l

    def __getitem__(self, i):
        """
        return i-th node <==> l[i]

        """
        assert -1 <= i <= self.n
        p = self.head
        k = -1
        while k < i:
            p = p.next
            k += 1
        return p

    def lookup(self, data):
        """
        look up the node containing data

        """
        p = self.head.next
        while p != self.tail:
            if p.data == data:
                return p
            else:
                p = p.next
        return None


    def insert(self, i, data):
        """
        insert a new node containing data at i-th location

        """
        assert 0 <= i <= self.n
        node = Node(data)
        prev = self[i - 1]
        next = prev.next
        node.next = next
        prev.next = node
        self.n += 1

    def remove(self, i):
        """
        delete i-th node

        """
        assert 0<= i < self.n
        prev = self[i - 1]
        node = prev.next
        data = prev.next.data
        prev.next = prev.next.next
        self.n -= 1
        del node
        return data


class TestList():
    def test_init(self):
        l = List()
        assert l.list() == []

    def test_initwithlist(self):
        l = List([1, 2, 3])
        assert l.list() == [1, 2, 3]
        assert l.n == 3

    def test_list(self):
        l = List()

    def test_idx(self):
        l = List()
        assert l[-1] == l.head
        assert l[0] == l.tail
        l.insert(0, 0)
        l.insert(1, 1)
        assert l[0].data == 0
        assert l[1].data == 1

    def test_lookup(self):
        l = List()
        assert l.lookup(7) == None

    def test_insert(self):
        l = List()
        l.insert(0, 0)
        assert l.list() == [0]
        l.insert(1, 1)
        assert l.list() == [0, 1]
        l.insert(1, 2)
        assert l.list() == [0, 2, 1]

    def test_remove(self):
        l = List()
        for i, data in enumerate([0, 1, 2, 3]):
            l.insert(i, data)
        assert l.list() == [0, 1, 2, 3]
        assert l.remove(1) == 1
        assert l.list() == [0, 2, 3]
        assert l.remove(0) == 0
        assert l.list() == [2, 3]
        assert l.remove(1) == 3
        assert l.list() == [2]
