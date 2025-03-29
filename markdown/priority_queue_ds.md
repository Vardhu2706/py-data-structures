# Priority Queue Data Structure

```python
```python
# Priority Queue Data Structure

## 1. Concept Overview

"""
A Priority Queue is an abstract data type similar to a regular queue or stack data structure, but where each element has a "priority" associated with it. In a priority queue, an element with high priority is served before an element with low priority. If two elements have the same priority, they are served according to their order in the queue.

Priority queues are commonly implemented using heaps due to their efficient access and manipulation of the highest (or lowest) priority element. The most common type of heap is a binary heap, which supports logarithmic time complexity for insertion and deletion of elements.
"""

## 2. Implementation Details

"""
Priority Queues can be implemented using various underlying data structures, such as:
- Binary Heaps: Most common and efficient, providing O(log n) time complexity for insertions and deletions.
- Fibonacci Heaps: Provide better amortized time complexity for decrease-key operations.
- Balanced Binary Search Trees: Offer O(log n) time complexity for all operations, including updates.

The binary heap implementation, specifically a min-heap or max-heap, is widely used due to its simplicity and efficiency. In a min-heap, the smallest element is always at the root, whereas, in a max-heap, the largest element is at the root.
"""

## 3. Core Operations & Time Complexities

"""
Key operations for a priority queue include:
- Insertion: Adding a new element with a specific priority. Time Complexity: O(log n)
- Deletion: Removing the element with the highest priority (min or max). Time Complexity: O(log n)
- Peek/Top: Retrieving the element with the highest priority without removing it. Time Complexity: O(1)
- Change Priority: Updating the priority of an element. Time Complexity: O(log n) for heap implementations.
"""

## 4. Common Use Cases

"""
- Task Scheduling: Prioritizing tasks based on importance or deadlines.
- Dijkstra's Algorithm: Finding the shortest path in a graph.
- A* Search Algorithm: Pathfinding and graph traversal algorithm.
- Bandwidth Management: Allocating resources to high-priority tasks.
- Simulation Systems: Managing events in discrete event simulations.
"""

## 5. Trade-offs

"""
- Complexity: Priority queues can be more complex to implement and manage compared to regular queues or stacks.
- Overhead: Maintaining the heap property can introduce computational overhead.
- Limited Operations: Unlike other data structures, priority queues primarily support prioritized access rather than arbitrary access.
"""

## 6. Design Decisions

"""
- Choosing the right underlying data structure (e.g., binary heap vs. Fibonacci heap) based on the application requirements.
- Deciding between a min-heap and a max-heap depending on whether the highest or lowest priority element is needed for quick access.
"""

## 7. Visual / Intuition

"""
Visualize a priority queue implemented as a binary heap:
- Imagine a binary tree where each parent node has a value less than or equal to (or greater than or equal to, in the case of a max-heap) its children.
- This structure allows quick access to the root element, which is the highest (or lowest) priority element.
- When inserting or deleting an element, the tree is adjusted to maintain the heap property.
"""

## 8. Programming Patterns

"""
- Heap Sort: Utilize the properties of a priority queue to sort a collection of elements.
- Event Simulation: Use a priority queue to manage and execute scheduled events.
- Lazy Evaluation: Defer computation of expensive operations using priority-based scheduling.
"""

## 9. Typical Problems

"""
- Implementing Dijkstra's or A* algorithms for pathfinding.
- Managing real-time scheduling systems where tasks have varying priorities.
- Simulating systems where events are triggered based on priority.
"""

## 10. Gotchas / Pitfalls

"""
- Forgetting to maintain the heap property during insertions and deletions can lead to incorrect behavior.
- Priority queues do not support direct access to arbitrary elements, which can be limiting in certain scenarios.
- Be cautious of integer overflow when dealing with absolute priorities in certain applications.
"""

## 11. Code Implementation (Demo of Core Operations)

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def insert(self, item, priority):
        """Insert an item with a given priority."""
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def delete(self):
        """Remove and return the item with the highest priority."""
        return heapq.heappop(self._queue)[-1]

    def peek(self):
        """Return the item with the highest priority without removing it."""
        return self._queue[0][-1]

# Example usage
pq = PriorityQueue()
pq.insert('task1', 1)
pq.insert('task2', 3)
pq.insert('task3', 2)

print("Top priority item:", pq.peek())  # Output: 'task1'
print("Removed item:", pq.delete())     # Output: 'task1'
print("Next top priority item:", pq.peek())  # Output: 'task3'
```
```