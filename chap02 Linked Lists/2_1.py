#!/usr/bin/env python

"""
Write code to remove duplicates from an unsorted linked list.

Q: singly? doubly?

- naive. For every node, remove duplicates from left other parts.
- sort and remove duplicates.
- use hash tables to keep track of visited nodes.

FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

solution 1 works without temporary buffer.
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'linked-lists'))

from singly_linked_list import Node


# TODO
