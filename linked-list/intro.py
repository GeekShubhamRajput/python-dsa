## Linked List

# A Linked List is a linear data structure where elements are stored in nodes.
# Each node contains:
# Data — the value stored in the node.
# Next — a reference to the next node.

# Unlike arrays, linked-list elements are not required to be stored next to each other in memory.

# [10 | next] → [20 | next] → [30 | None]

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

first = Node(10)
second = Node(20)
third = Node(30)

first.next = second
second.next = third

# first → 10 → 20 → 30 → None

## Advantages
# - Dynamic size
# - Easy insertion and deletion when the node/reference is known
# - No need for contiguous memory

## Disadvantages
# - No direct/random access like array[2]
# - Extra memory is required for references
# - Searching for an element takes O(n) time
