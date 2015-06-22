from tree import Node

def test_init():
    root = Node(8)
    assert root.data == 8

def test_insert():
    root = Node(8)
    root.insert(3)
    root.insert(10)
    assert root.left.data == 3
    assert root.right.data == 10

def test_lookup():
    root = Node(8)
    root.insert(3)
    root.insert(10)
    assert root.lookup(8) == (root, None)
    assert root.lookup(3) == (root.left, root)
    assert root.lookup(10) == (root.right, root)

def test_delete():
    root = Node(8)
    root.insert(3)
    root.delete(3)
    root.delete(8)

# root.insert(3)
# root.insert(10)
# root.insert(1)
# root.insert(6)
# root.insert(4)
# root.insert(7)
# root.insert(14)
# root.insert(13)
