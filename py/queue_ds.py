# Queue Data Structure

## 1. Concept Overview

"""
A queue is a linear data structure that follows the First In First Out (FIFO) principle.
This means that the element inserted first will be the first one to be removed.
Queues are used in scenarios where order needs to be preserved, such as scheduling tasks,
handling requests, or managing resources that are shared among multiple consumers.
"""

## 2. Implementation Details

"""
Queues can be implemented using arrays (lists in Python) or linked lists. In a queue,
elements are added at the rear (end) and removed from the front (beginning). When using
arrays, care must be taken to manage the space efficiently, often requiring dynamic resizing
or circular buffer techniques to avoid wasted space. Linked list implementations naturally
support dynamic resizing and do not require shifting elements.
"""

## 3. Core Operations & Time Complexities

"""
The core operations of a queue include:

- Enqueue: Add an element to the rear of the queue. O(1) time complexity.
- Dequeue: Remove an element from the front of the queue. O(1) time complexity.
- Peek/Front: Retrieve the front element without removing it. O(1) time complexity.
- IsEmpty: Check whether the queue is empty. O(1) time complexity.
- Size: Get the number of elements in the queue. O(1) time complexity.
"""

## 4. Common Use Cases

"""
Queues are commonly used in:

- Task scheduling, such as CPU task scheduling or print job management.
- Breadth-first search (BFS) algorithms in graph traversal.
- Asynchronous data processing pipelines.
- Simulations of real-world queues, like supermarket checkouts or buffer management.
"""

## 5. Trade-offs

"""
The main trade-off in a queue implementation is between time complexity and memory usage.
An array-based implementation may waste space or require resizing, whereas a linked list
implementation uses more memory per element due to pointers but doesn't require resizing.
The choice of implementation may depend on specific performance and memory constraints.
"""

## 6. Design Decisions

"""
When designing a queue, consider the following:

- Whether to implement it as a circular buffer to optimize space in an array-based queue.
- Use of doubly vs. singly linked lists if a linked-list implementation is chosen.
- Whether additional operations, such as priority or sorting, are required, leading to
  variations like priority queues or double-ended queues (deques).
"""

## 7. Visual / Intuition

"""
Imagine a queue as a line of people waiting to enter a theater. The person at the front
of the line enters first (dequeue), and new arrivals join the end of the line (enqueue).
This visualization helps to understand the FIFO behavior of queues.
"""

## 8. Programming Patterns

"""
Common programming patterns involving queues include:

- Level-order traversal of trees, where nodes are processed level by level.
- Implementation of service-oriented architectures where requests are queued for processing.
- Breadth-first search, where nodes in a graph are explored layer by layer.
"""

## 9. Typical Problems

"""
- Implementing a queue with basic operations.
- Using a queue to perform level-order traversal of a binary tree.
- Solving problems that require the processing of items in the order they arrive, such as
  customer service systems or call centers.
"""

## 10. Gotchas / Pitfalls

"""
- Ensure that the queue does not grow beyond available memory, especially in array-based
  implementations where resizing is not automatically handled.
- When implementing with linked lists, ensure proper handling of pointers to avoid memory
  leaks or invalid memory access.
- Be cautious with circular queue implementations to correctly manage indices.
"""

## 11. Code Implementation (Demo of Core Operations)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return an item from the front of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.pop(0)

    def peek(self):
        """Return the front item of the queue without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.items[0]

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Front item:", queue.peek())  # Output: Front item: 1
print("Queue size:", queue.size())  # Output: Queue size: 3

print("Dequeue item:", queue.dequeue())  # Output: Dequeue item: 1
print("Queue size after dequeue:", queue.size())  # Output: Queue size after dequeue: 2
