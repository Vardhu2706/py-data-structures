# Min Heap Data Structure

## 1. Concept Overview

"""
A Min Heap is a type of binary heap data structure where the root node is the smallest element. 
This property must be true for every subtree, meaning each parent node must be less than or equal to its child nodes.
Min Heaps are often used to implement priority queues where the highest priority element is the smallest one.
The structure allows efficient retrieval and removal of the minimum element.
"""

## 2. Implementation Details

"""
A Min Heap is typically implemented using an array where:
- The root element is at index 0.
- For any element at index i, its left child is at index 2*i + 1 and its right child is at index 2*i + 2.
- The parent of any element at index i is located at index (i-1)//2.

The heap property is maintained through two primary operations: 'heapify up' and 'heapify down'.
- 'Heapify up' is used during insertion to maintain the heap property by comparing a node with its parent and swapping if necessary.
- 'Heapify down' is used during deletion to maintain the heap property by comparing a node with its children and swapping with the smaller child if necessary.
"""

## 3. Core Operations & Time Complexities

"""
1. Insert:
   - Time Complexity: O(log n), where n is the number of elements in the heap.
   - Description: Add the new element at the end of the heap and perform 'heapify up' to restore the heap property.

2. Extract Min:
   - Time Complexity: O(log n)
   - Description: Remove the root element (minimum), replace it with the last element, and perform 'heapify down' to restore the heap property.

3. Peek Min:
   - Time Complexity: O(1)
   - Description: Retrieve, but do not remove, the root element (minimum) of the heap.
"""

## 4. Common Use Cases

"""
1. Priority Queues:
   Min Heaps are used to implement priority queues where the element with the highest priority (smallest value) is served first.

2. Scheduling Algorithms:
   Used in operating systems for job scheduling where tasks with the shortest time are executed first.

3. Graph Algorithms:
   Utilized in algorithms like Dijkstra's shortest path and Prim's minimum spanning tree to efficiently retrieve the smallest element.
"""

## 5. Trade-offs

"""
- Pros:
  - Provides O(1) time complexity for retrieving the minimum element.
  - Ensures O(log n) time complexity for insertion and removal operations.

- Cons:
  - Not suitable for searching arbitrary elements as the search operation is O(n).
  - Requires additional space for the array representation, but generally efficient for the operations it supports.
"""

## 6. Design Decisions

"""
- Array-based implementation is chosen for its simplicity and efficiency in managing parent-child relationships through index calculations.
- The choice of using 0-based indexing helps in simplifying arithmetic for parent and child calculations.
"""

## 7. Visual / Intuition

"""
Consider a Min Heap as a binary tree where each level of the tree is filled from left to right.
The smallest element is always at the root. Visualizing the heap as a complete binary tree helps in understanding its balanced nature and efficient operations.
"""

## 8. Programming Patterns

"""
- Recursive and iterative approaches can be used for heapify operations.
- Use of dynamic arrays (lists in Python) to allow the heap to resize as elements are added or removed.
"""

## 9. Typical Problems

"""
1. Implementing a priority queue using a Min Heap.
2. Finding the kth smallest element in an array.
3. Merging k sorted lists or arrays efficiently.
"""

## 10. Gotchas / Pitfalls

"""
- Failing to maintain the heap property during insertions or deletions can lead to incorrect results.
- Off-by-one errors are common in index calculations for parent-child relationships.
- Remember that the array must be a complete binary tree to effectively utilize the heap's properties.
"""

## 11. Code Implementation (Demo of Core Operations)

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, element):
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            raise IndexError("extract_min(): empty heap")
        min_elem = self.heap[0]
        last_elem = self.heap.pop()
        if self.heap:
            self.heap[0] = last_elem
            self._heapify_down(0)
        return min_elem

    def peek_min(self):
        if not self.heap:
            raise IndexError("peek_min(): empty heap")
        return self.heap[0]

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        smallest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

# Example usage:
heap = MinHeap()
heap.insert(10)
heap.insert(5)
heap.insert(3)
print(heap.extract_min())  # Outputs: 3
print(heap.peek_min())     # Outputs: 5
