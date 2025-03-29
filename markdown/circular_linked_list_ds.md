# Circular Linked List Data Structure

```python
```python
# Circular Linked List Data Structure

## 1. Concept Overview

"""
A Circular Linked List is a variation of a linked list where the last node points back to the first node, forming a circle.
Unlike a traditional singly linked list, this structure allows for efficient traversal and operations that require wrapping around 
the end of the list back to the beginning, without the need for null termination. This cyclic nature makes it suitable for 
applications requiring a circular traversal pattern.

Each node in a circular linked list contains two components:
- Data: The information stored in the node.
- Next: A reference to the next node in the list.

The head of the list points to the first node, and the last node's next reference points back to the head, closing the loop.
"""

## 2. Implementation Details

"""
To implement a circular linked list, a class `Node` is created to represent each element, containing data and a reference to the next node.
The `CircularLinkedList` class manages the list with operations to insert, delete, and traverse nodes. It maintains a reference to the 
head of the list. The last node's next reference is updated as necessary to maintain the circular linkage.
"""

## 3. Core Operations & Time Complexities

"""
1. Insert at Beginning: O(1)
   Inserts a new node right after the head and updates the last node's next reference if necessary.

2. Insert at End: O(n)
   Traverses to the last node and inserts a new node after it, updating the last node's next reference to the head.

3. Delete a Node: O(n)
   Searches for a node with the specified value and removes it by updating the previous node's next reference. 
   Special care is taken when the node to be deleted is the head or the last node.

4. Traverse: O(n)
   Visits each node in the list starting from the head until it returns to the head, allowing for processing or displaying of node data.
"""

## 4. Common Use Cases

"""
- Round Robin Scheduling: Commonly used in CPU scheduling and other cyclic tasks where processes must be managed in a circular queue.
- Multiplayer Games: To manage players in a game circle or turn-based systems.
- Circular Buffers: Used in buffering data streams, allowing for efficient memory usage.
"""

## 5. Trade-offs

"""
- Pros:
  - No need for null checks in traversal, simplifying logic.
  - Circular nature allows for elegant handling of cyclic processes.

- Cons:
  - More complex insertion and deletion logic compared to singly linked lists.
  - Care must be taken to maintain the circular linkage, especially during modifications.
"""

## 6. Design Decisions

"""
Choosing a circular linked list often depends on the application's need for cyclic operations and efficient traversal 
without the overhead of checking for list termination. It balances between simplicity and the need for a flexible, 
non-linear data structure.
"""

## 7. Visual / Intuition

"""
Visualize a circular linked list as a circle of nodes. Starting from any node, you can traverse through each node and 
eventually return to the starting node, forming a closed loop. This visual model helps in understanding the modularity 
and continuous flow of operations.
"""

## 8. Programming Patterns

"""
- Sentinel or Dummy Nodes: Sometimes used to simplify boundary conditions for insertion and deletion.
- Tortoise and Hare Algorithm: A common pattern used on circular lists to detect cycles or find loop lengths.
"""

## 9. Typical Problems

"""
- Detecting loops in a linked list.
- Implementing a circular buffer.
- Rotating a list by k nodes.
- Simulating a Round Robin scheduling system.
"""

## 10. Gotchas / Pitfalls

"""
- Forgetting to update the last node's reference when modifying the list can break the circular nature.
- Infinite loops can occur if traversal does not account for the circular structure properly.
- Edge cases such as an empty list or a list with a single node need careful consideration.
"""

## 11. Code Implementation (Demo of Core Operations)

class Node:
    """A Node in a Circular Linked List."""
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    """Circular Linked List with core operations."""
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def delete_node(self, key):
        if self.head is None:
            return

        current = self.head
        prev = None

        # If the node to be deleted is the head node
        if current.data == key:
            while current.next != self.head:
                current = current.next
            if self.head == self.head.next:
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
            return

        prev = self.head
        current = self.head.next
        while current != self.head:
            if current.data == key:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def traverse(self):
        if not self.head:
            return []
        elements = []
        current = self.head
        while True:
            elements.append(current.data)
            current = current.next
            if current == self.head:
                break
        return elements

# Example Usage
cll = CircularLinkedList()
cll.insert_at_beginning(3)
cll.insert_at_beginning(2)
cll.insert_at_end(4)
cll.insert_at_end(5)
print(cll.traverse())  # Output: [2, 3, 4, 5]
cll.delete_node(3)
print(cll.traverse())  # Output: [2, 4, 5]
```
```