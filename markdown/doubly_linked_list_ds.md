# Doubly Linked List Data Structure

```python
```python
# Doubly Linked List Data Structure

## 1. Concept Overview

"""
A Doubly Linked List is a type of data structure consisting of a sequence of elements, each containing a reference to both the next and previous elements in the sequence. This structure allows for efficient insertion and deletion of nodes from both ends of the list, as well as from the middle, without the need to shift elements, as would be necessary in an array.

Doubly Linked Lists are particularly advantageous when bidirectional traversal is needed, as each node maintains a reference to its predecessor and successor.
"""

## 2. Implementation Details

"""
In a Doubly Linked List, each node is encapsulated in an object with attributes for data storage, a pointer to the next node, and a pointer to the previous node. The list itself maintains references to the head and tail nodes for efficient access and modification.

The typical operations on a Doubly Linked List include:
- Insertion: Adding nodes at various positions.
- Deletion: Removing nodes from the list.
- Traversal: Accessing nodes to read or modify their values.
"""

## 3. Core Operations & Time Complexities

"""
1. Insertion
   - At the beginning: O(1)
   - At the end: O(1)
   - At a specific position: O(n)

2. Deletion
   - From the beginning: O(1)
   - From the end: O(1)
   - From a specific position: O(n)

3. Search
   - Best-case: O(1)
   - Worst-case: O(n)

4. Traversal: O(n)
"""

## 4. Common Use Cases

"""
- Implementing LRU (Least Recently Used) caches.
- Undo functionality in applications, where each operation can be navigated forwards and backwards.
- Navigation systems where both forward and backward movement is required.
"""

## 5. Trade-offs

"""
- Doubly Linked Lists require extra memory for storing two pointers (next and previous) per node compared to singly linked lists.
- They provide more flexibility in terms of traversal and modification but at the cost of increased memory usage.
- In scenarios where bidirectional traversal is unnecessary, a singly linked list may be more efficient.
"""

## 6. Design Decisions

"""
Key design considerations when implementing a Doubly Linked List include:
- Whether to maintain references to both head and tail nodes, which can optimize access and insertion operations.
- Deciding how to handle boundary conditions, such as inserting or deleting from an empty list.
- Ensuring robust handling of node pointers to avoid memory leaks or segmentation faults.
"""

## 7. Visual / Intuition

"""
Consider a train where each car is connected to both the car in front and behind. This setup allows passengers to move forwards and backwards, akin to how nodes in a doubly linked list are connected.
"""

## 8. Programming Patterns

"""
- Sentinel Nodes: Use of dummy head and tail nodes to simplify edge-case handling for insertion and deletion operations.
- Iterator Pattern: Implementing an iterator to traverse the list forwards or backwards.
"""

## 9. Typical Problems

"""
- Implementing LRU Cache using a doubly linked list and a hash map.
- Reversing a doubly linked list.
- Detecting and removing cycles in a doubly linked list.
"""

## 10. Gotchas / Pitfalls

"""
- Failing to update both next and previous pointers during insertion and deletion can lead to broken links.
- Properly managing memory, especially in languages without automatic garbage collection, to avoid memory leaks.
- Being cautious with boundary conditions, such as operations on an empty list or single-node list.
"""

## 11. Code Implementation (Demo of Core Operations)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete_from_beginning(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return data

    def delete_from_end(self):
        if self.tail is None:
            return None
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return data

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=' ')
            current = current.prev
        print()

# Example usage:
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_beginning(5)
dll.display_forward()  # Outputs: 5 10 20
dll.display_backward() # Outputs: 20 10 5
dll.delete_from_beginning()
dll.display_forward()  # Outputs: 10 20
dll.delete_from_end()
dll.display_forward()  # Outputs: 10
```
```