#!/usr/bin/env python

from ffilib import ffilib

ffi, lib = openlib('singly-linked-list')

def test_stack():
    l = lib.mklist()

    # push node 1
    lib.stack_push(l, 1)
    assert l.head.data == 1

    # push node 2
    lib.stack_push(l, 2)
    assert l.head.data == 2
    assert l.head.next.data == 1

    # pop node 2
    assert lib.stack_pop(l) == 2
    assert l.head.data == 1


def test_queue():
    l = lib.mklist()

    # add node 1
    lib.queue_add(l, 1)
    assert l.head.data == 1

    # add node 2
    lib.queue_add(l, 2)
    assert l.head.data == 1
    assert l.head.next.data == 2

    # remove node 1
    assert lib.queue_remove(l) == 1
    assert l.head.data == 2

    # remove node 2
    assert lib.queue_remove(l) == 2

def test_list():
    l = lib.mklist()
    # insert node 0
    lib.list_insert(l, 0, 0);
    assert l.head.data == 0

    # insert node 1
    lib.list_insert(l, 1, 1);
    assert l.head.data == 0
    assert l.head.next.data == 1

    # insert node 2
    lib.list_insert(l, 1, 2);
    assert l.head.data == 0
    assert l.head.next.data == 2
    assert l.head.next.next.data == 1

    # remove node 2
    assert lib.list_delete(l, 1) == 2
    assert l.head.data == 0
    assert l.head.next.data == 1

    # remove node 0
    assert lib.list_delete(l, 0) == 0
    assert l.head.data == 1
