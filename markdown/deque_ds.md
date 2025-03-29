# Deque Data Structure

```python
```python
# Deque Data Structure

## 1. Concept Overview

"""
A deque (short for "double-ended queue") is a linear data structure that allows insertion and deletion of elements from both ends, 
the front and the rear. Unlike stacks and queues, which are restricted data structures, deques are more flexible and can be used in
situations where elements need to be accessed, added, or removed from both ends efficiently.

Deques support all operations that stacks and queues support, making them versatile in handling a variety of problems. They are often 
implemented as a doubly linked list or a dynamic array, allowing for O(1) time complexity for all operations at both ends.
"""

## 2. Implementation Details

"""
A deque can be implemented using a doubly linked list or a dynamic array (like Python's built-in list). 
In a doubly linked list implementation, each element points to both its previous and next element, allowing constant-time insertions 
and deletions at both ends. In a dynamic array implementation, care must be taken to handle resizing of the array when it becomes full.

The choice between these implementations typically depends on the specific requirements of the application, such as memory usage and 
the frequency of operations at either end.
"""

## 3. Core Operations & Time Complexities

"""
1. add_front(item): Inserts an item at the front of the deque. [O(1)]
2. add_rear(item): Inserts an item at the rear of the deque. [O(1)]
3. remove_front(): Removes and returns the front item from the deque. [O(1)]
4. remove_rear(): Removes and returns the rear item from the deque. [O(1)]
5. peek_front(): Returns the front item without removing it. [O(1)]
6. peek_rear(): Returns the rear item without removing it. [O(1)]
7. is_empty(): Checks if the deque is empty. [O(1)]
8. size(): Returns the number of elements in the deque. [O(1)]
"""

## 4. Common Use Cases

"""
- Implementing both stack and queue operations using a single data structure.
- Maintaining a list of recent elements accessed, such as in caching mechanisms.
- Handling sliding window scenarios, often used in algorithms involving contiguous subarrays.
- Palindrome checking, where elements are compared from both ends towards the center.
"""

## 5. Trade-offs

"""
- Memory Usage: If implemented as a doubly linked list, additional memory is required for pointers. If implemented as a dynamic array,
  resizing and shifting can lead to overhead.
- Complexity: Although flexible, deques may be more complex to implement and understand compared to basic stacks and queues.
- Choice of Implementation: The choice between linked list and array implementations can affect performance based on the nature of
  operations performed frequently (e.g., frequent access vs frequent insertions/deletions).
"""

## 6. Design Decisions

"""
- Representation: Choosing between a doubly linked list or dynamic array representation based on expected operation patterns.
- Circular Buffers: When implemented as a circular buffer, additional logic is needed to handle wrap-around cases.
- Dynamic Resizing: If using arrays, deciding on resizing strategies (e.g., doubling the size when full) is crucial for performance.
"""

## 7. Visual / Intuition

"""
Visualize a deque as a train with open ends, where new cars can be added or removed from either the front or the rear. 
This flexibility allows it to adapt like a queue or stack as needed, making it suitable for various scenarios.
"""

## 8. Programming Patterns

"""
- Double-ended Traversal: Using a deque to traverse elements from both ends, often used in palindrome problems.
- Sliding Window: Maintaining a window of elements and updating it efficiently as it slides over a data set.
- Level Order Traversal: In tree structures, using a deque to facilitate level-order traversal by adding children to the rear.
"""

## 9. Typical Problems

"""
- Implementing a maximum/minimum sliding window for an array.
- Designing an LRU (Least Recently Used) cache.
- Palindrome validation by comparing elements from both ends.
- Breadth-first search (BFS) in graphs using a deque for node exploration.
"""

## 10. Gotchas / Pitfalls

"""
- When using dynamic arrays, be cautious of the overhead associated with resizing when the array becomes full.
- Properly handle edge cases such as removing elements from an empty deque to avoid errors.
- Be mindful of the trade-offs between memory usage and performance based on the implementation choice.
"""

## 11. Code Implementation (Demo of Core Operations)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def add_front(self, item):
        new_node = Node(item)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self._size += 1

    def add_rear(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def remove_front(self):
        if self.is_empty():
            raise IndexError("remove_front from empty deque")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        self._size -= 1
        return value

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("remove_rear from empty deque")
        value = self.rear.value
        self.rear = self.rear.prev
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None
        self._size -= 1
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("peek_front from empty deque")
        return self.front.value

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("peek_rear from empty deque")
        return self.rear.value

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

# Example Usage
deque = Deque()
deque.add_rear(10)
deque.add_front(20)
deque.add_rear(30)
print(deque.peek_front())  # Output: 20
print(deque.peek_rear())   # Output: 30
print(deque.remove_front()) # Output: 20
print(deque.remove_rear())  # Output: 30
print(deque.size())         # Output: 1
```
```