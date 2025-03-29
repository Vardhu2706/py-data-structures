# Max Heap Data Structure

## 1. Concept Overview

"""
A Max Heap is a complete binary tree where the value of each node is greater than or equal to the values of its children. This ensures that the largest element is always at the root of the tree. Max Heaps are commonly used to implement priority queues, where the highest priority element is always served first.
"""

## 2. Implementation Details

"""
A Max Heap can be efficiently implemented using an array. The root element is at index 0. For any element at index i:
- The left child is located at index 2*i + 1
- The right child is located at index 2*i + 2
- The parent node is located at index (i-1) // 2

The heap property is maintained through operations like 'heapify', which adjusts the elements to satisfy the max heap condition after an insertion or deletion.
"""

## 3. Core Operations & Time Complexities

"""
1. Insert: O(log n) - Inserting a new element and maintaining the heap property.
2. Delete (typically delete the max): O(log n) - Removing the root element, replacing it with the last element, and adjusting the heap.
3. Peek (get max): O(1) - Accessing the root element without removing it.
4. Heapify: O(n) - Building a heap from an unsorted array.
"""

## 4. Common Use Cases

"""
- Implementing a priority queue.
- Sorting algorithms like Heap Sort.
- Scheduling problems where tasks need to be processed based on priority.
- Graph algorithms like Dijkstra's shortest path and Prim's minimum spanning tree.
"""

## 5. Trade-offs

"""
- Max Heaps provide efficient access to the maximum element but do not support fast access for elements other than the root.
- Insertion and deletion operations are efficient, but maintaining the complete binary tree structure can require shifting elements.
- Max Heaps are not suitable for operations that require fast random access to arbitrary elements.
"""

## 6. Design Decisions

"""
- Choosing an array-based implementation over a tree-based (linked node) representation because of lower overhead and better cache performance.
- Deciding to heapify from bottom to top for efficient insert operations.
- Implementing a sift-up (bubble-up) and sift-down (bubble-down) approach to maintain heap property during insertions and deletions.
"""

## 7. Visual / Intuition

"""
Imagine a binary tree where each parent node has a higher value than its children, creating a pyramid-like structure. When viewing the heap as an array, think of it as a level-order traversal of this binary tree.
"""

## 8. Programming Patterns

"""
- Use of heapify operations to maintain structural and heap properties during modifications.
- Leveraging array indices to navigate parent-child relationships.
"""

## 9. Typical Problems

"""
- Implementing a system that prioritizes tasks or resources.
- Solving problems related to finding the 'k' largest elements.
- Optimizing resource allocation based on priority.
"""

## 10. Gotchas / Pitfalls

"""
- Forgetting to maintain the complete binary tree structure can lead to inefficient operations.
- Miscalculating indices during sift-up or sift-down can lead to incorrect heap properties.
- Assuming the heap is always fully balanced; it is complete but not necessarily fully balanced.
"""

## 11. Code Implementation (Demo of Core Operations)

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, element):
        """Insert an element into the heap."""
        self.heap.append(element)
        self._sift_up(len(self.heap) - 1)

    def delete_max(self):
        """Remove and return the largest element from the heap."""
        if len(self.heap) == 0:
            raise IndexError("delete_max(): empty heap")
        max_element = self.heap[0]
        last_element = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_element
            self._sift_down(0)
        return max_element

    def peek(self):
        """Return the largest element from the heap."""
        if len(self.heap) == 0:
            raise IndexError("peek(): empty heap")
        return self.heap[0]

    def _sift_up(self, index):
        """Move the element at index up to restore heap property."""
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._sift_up(parent_index)

    def _sift_down(self, index):
        """Move the element at index down to restore heap property."""
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child

        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._sift_down(largest)

# Example usage:
# max_heap = MaxHeap()
# max_heap.insert(10)
# max_heap.insert(20)
# max_heap.insert(5)
# print(max_heap.peek()) # Output: 20
# print(max_heap.delete_max()) # Output: 20
# print(max_heap.peek()) # Output: 10
