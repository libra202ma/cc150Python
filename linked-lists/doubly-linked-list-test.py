#!/usr/bin/env python

from ffilib import ffilib

ffi, lib = ffilib('doubly-linked-list')

def test_mklist():
    l = lib.mklist()
    assert l.n == 1
    assert l.dummy.data == 0
    assert l.dummy.prev == l.dummy
    assert l.dummy.next == l.dummy

def test_idx():
    l = lib.mklist()
    assert lib.idx(l, 0) == l.dummy
    lib.insert(l, 1, 1)
    assert lib.idx(l, 1) == l.dummy.next

def test_get():
    l = lib.mklist()
    lib.insert(l, 1, 1)
    lib.insert(l, 1, 2)
    assert lib.get(l, 1) == 2
    assert lib.get(l, 2) == 1

def test_set():
    l = lib.mklist()
    lib.insert(l, 1, 1)
    lib.set(l, 1, 10)
    assert lib.get(l, 1) == 10

def test_insert():
    l = lib.mklist()
    lib.insert(l, 1, 1)
    assert l.n == 2
    assert l.dummy.next.data == 1
    assert l.dummy.prev.data == 1
    lib.insert(l, 1, 2)
    assert l.n == 3
    assert l.dummy.next.data == 2
    assert l.dummy.next.next.data == 1
    assert l.dummy.prev.data == 1
    assert l.dummy.prev.prev.data == 2

def test_delete():
    l = lib.mklist()
    lib.insert(l, 1, 1)
    assert lib.delete(l, 1) == 1
    lib.insert(l, 1, 1)
    lib.insert(l, 2, 2)
    assert lib.delete(l, 1) == 1
    assert lib.get(l, 1) == 2
    assert lib.delete(l, 1) == 2
