# Singly Linked List Data Structure

## 1. Concept Overview

"""
A singly linked list is a linear data structure consisting of nodes. Each node contains two elements: data and a reference to the next node in the sequence. The list starts with a head node, and the last node in the list points to None, indicating the end of the list. Unlike arrays, linked lists do not store elements in contiguous memory locations, which allows for efficient insertions and deletions without reallocating or reorganizing the entire structure.
"""

## 2. Implementation Details

"""
A singly linked list is implemented using nodes, where each node is an instance of a class containing data and a reference to the next node. The linked list itself maintains a reference to the head node. Operations such as insertion, deletion, and traversal are performed by manipulating these references.
"""

## 3. Core Operations & Time Complexities

"""
- Insertion at the beginning: O(1)
- Insertion at the end: O(n)
- Deletion from the beginning: O(1)
- Deletion from the end: O(n)
- Search for an element: O(n)
- Traversal: O(n)
"""

## 4. Common Use Cases

"""
- Dynamic memory allocation where size can vary.
- Implementing queues, stacks, and other abstract data types.
- Situations where frequent insertions and deletions are necessary.
- Applications requiring constant-time insertions/deletions from the list's head.
"""

## 5. Trade-offs

"""
- Pros:
  - Efficient insertions and deletions at the beginning.
  - Dynamic size, not limited by initial capacity.
  
- Cons:
  - Inefficient access time for elements, requiring O(n) for traversal.
  - Extra memory overhead for storing references.
  - More complex than arrays for certain operations.
"""

## 6. Design Decisions

"""
- Choosing between singly and doubly linked lists: A singly linked list is simpler but offers less flexibility for bidirectional traversal and deletion.
- Managing memory: Careful consideration is required to manage memory effectively and avoid leaks, especially in languages without automatic garbage collection.
"""

## 7. Visual / Intuition

"""
Visualize a singly linked list as a series of nodes connected linearly. Each node points to the next node, forming a chain. This structure is analogous to a treasure hunt where each clue leads to the next clue until the end.
"""

## 8. Programming Patterns

"""
- Iterative traversal pattern: Using a loop to traverse each node starting from the head until reaching the end (None).
- Recursive operations: Some operations can be expressed recursively, although this is less common due to potential stack overflow issues in large lists.
"""

## 9. Typical Problems

"""
- Implementing list reversal.
- Detecting cycles within a linked list.
- Merging two sorted linked lists.
- Finding the intersection of two linked lists.
"""

## 10. Gotchas / Pitfalls

"""
- Avoiding the loss of the head reference during operations, which can lead to losing access to the entire list.
- Ensuring proper handling of edge cases, such as empty lists or single-node lists, during insertions and deletions.
- Maintaining correct node references after operations to prevent memory leaks or access violations.
"""

## 11. Code Implementation (Demo of Core Operations)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_from_beginning(self):
        """
        Delete a node from the beginning of the list.
        """
        if not self.head:
            return
        self.head = self.head.next

    def delete_from_end(self):
        """
        Delete a node from the end of the list.
        """
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def search(self, key):
        """
        Search for a node containing data that matches the key.
        """
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def traverse(self):
        """
        Traverse the list and print each element.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Example usage:
linked_list = SinglyLinkedList()
linked_list.insert_at_beginning(3)
linked_list.insert_at_end(5)
linked_list.insert_at_beginning(1)
linked_list.traverse() # Output: [1, 3, 5]
linked_list.delete_from_end()
linked_list.traverse() # Output: [1, 3]
linked_list.delete_from_beginning()
linked_list.traverse() # Output: [3]
