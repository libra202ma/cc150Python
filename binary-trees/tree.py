#!/usr/bin/env python

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def lookup(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def children_count(self):
        if self is None:
            return None
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

    def delete(self, data):
        node, parent = self.lookup(data)
        if node is not None:
            childen_count = node.children_count()
            if childen_count == 0:
                # if node has no children
                # simply set its parent pointer to None and free space
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                del node
            elif children_count == 1:
                # if node has 1 child
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                del node
            else:
                # node has 2 children
                parent = node
                # find successor
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                # replace node data by its successor data
                node.data = successor.data
                # fix successor's parent's child
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print self.data
        if self.right:
            self.right.print_tree()
