# Heap Data Structure

## 1. Concept Overview

"""
A Heap is a specialized tree-based data structure that satisfies the heap property. It comes in two variants:
- A Max-Heap where for any given node I, the value of I is greater than or equal to the values of its children. 
- A Min-Heap where for any given node I, the value of I is less than or equal to the values of its children.

Heaps are commonly implemented as binary trees and are typically used to implement priority queues due to their efficient access to the highest (or lowest) priority element.
"""

## 2. Implementation Details

"""
A Heap is generally implemented as a binary tree, but it is often represented using an array because it allows for efficient storage and access. 

For an element at index `i`:
- The parent is located at index `(i - 1) // 2`
- The left child is located at index `2 * i + 1`
- The right child is located at index `2 * i + 2`

Heaps are complete binary trees, meaning all levels are fully filled except possibly for the last, which is filled from left to right.
"""

## 3. Core Operations & Time Complexities

"""
1. Insertion:
   - Insert the element at the end of the heap and then "heapify" up.
   - Time Complexity: O(log n)

2. Deletion of the root (extract max/min):
   - Replace the root with the last element, remove the last element, and "heapify" down.
   - Time Complexity: O(log n)

3. Peek (Get max/min):
   - Simply return the root element.
   - Time Complexity: O(1)

4. Heapify:
   - Adjust the heap to maintain the heap property.
   - Time Complexity: O(log n) for insertion and deletion.
"""

## 4. Common Use Cases

"""
- Implementing priority queues.
- Scheduling algorithms.
- Graph algorithms like Dijkstra's and Prim's.
- Sorting algorithms such as heapsort.
"""

## 5. Trade-offs

"""
- Pros: Provides excellent access to the highest or lowest element, efficient insertion, and removal.
- Cons: Does not support search operations efficiently. Not suitable for finding arbitrary elements quickly.
"""

## 6. Design Decisions

"""
The choice between a Min-Heap and Max-Heap depends on the problem requirements:
- Use a Min-Heap when you need quick access to the smallest element.
- Use a Max-Heap when you need quick access to the largest element.

The array representation allows for efficient use of space and easy calculation of parent and child indices.
"""

## 7. Visual / Intuition

"""
Visualize a heap as a binary tree:
- For Max-Heap, each parent node is greater than its children.
- For Min-Heap, each parent node is smaller than its children.

This structure ensures that the highest (or lowest) priority element is always at the root for quick access.
"""

## 8. Programming Patterns

"""
- Heap Sort: Uses a heap to sort elements efficiently.
- Priority Queue: Provides queue operations based on priority instead of the arrival order.
"""

## 9. Typical Problems

"""
- Finding the k largest or smallest elements in an array.
- Merging k sorted arrays.
- Implementing a real-time scheduling algorithm.
"""

## 10. Gotchas / Pitfalls

"""
- Remember that a heap does not maintain a sorted order; it only guarantees the heap property.
- Be careful with off-by-one errors when calculating parent and child indices.
- A common mistake is to forget to "heapify" after inserting or removing elements.
"""

## 11. Code Implementation (Demo of Core Operations)

class Heap:
    def __init__(self, is_min_heap=True):
        self.heap = []
        self.is_min_heap = is_min_heap

    def _compare(self, first, second):
        if self.is_min_heap:
            return first < second
        else:
            return first > second

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self._compare(self.heap[index], self.heap[parent_index]):
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        size = len(self.heap)

        if left < size and self._compare(self.heap[left], self.heap[smallest]):
            smallest = left

        if right < size and self._compare(self.heap[right], self.heap[smallest]):
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def insert(self, element):
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)

    def extract(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def peek(self):
        return self.heap[0] if self.heap else None

# Example usage:
# max_heap = Heap(is_min_heap=False)
# max_heap.insert(10)
# max_heap.insert(5)
# max_heap.insert(3)
# print(max_heap.extract())  # Should print 10
