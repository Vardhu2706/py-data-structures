# Fibonacci Heap Data Structure

## 1. Concept Overview

"""
A Fibonacci Heap is a type of data structure that extends the functionality of a binomial heap. It supports a collection 
of trees that are loosely ordered and allows operation of merging heaps in a more efficient way. The key feature is that 
it provides better amortized time complexity for some operations compared to other heap structures. Fibonacci heaps are 
particularly known for their O(1) amortized time for operations like Insert and Decrease Key, and O(log n) for Delete 
Min and Delete operations. This makes them suitable for algorithms that require a lot of decrease key operations, such 
as Dijkstra's shortest path algorithm.
"""

## 2. Implementation Details

"""
The Fibonacci Heap is composed of a collection of heap-ordered trees. Each tree follows the min-heap property, meaning 
that the key of a node is greater than or equal to the key of its parent. The heap is maintained as a circular doubly 
linked list of trees, where each tree is represented by a root node. The key elements of a Fibonacci Heap are:

- Nodes: Each node in the heap maintains a parent, child, left, and right pointer to facilitate the heap operations.
- Min Node: A pointer to the node with the minimum key.
- Degree: The number of children a node has.
- Mark: A boolean flag used to assist in the decrease key operation.
"""

## 3. Core Operations & Time Complexities

"""
- Insert: O(1) amortized
  Insert a new tree into the heap by adding it to the root list.

- Find Min: O(1)
  Directly access the min node pointer to retrieve the minimum element.

- Union: O(1)
  Combine two heaps by concatenating their root lists and updating the min pointer.

- Extract Min: O(log n) amortized
  Remove the minimum element from the heap, reorganize trees by performing a series of link operations, and update the 
  min pointer.

- Decrease Key: O(1) amortized
  Decrease the key value of a node and potentially cut the node from its parent and add it to the root list if the heap 
  property is violated.

- Delete: O(log n) amortized
  Decrease the key to negative infinity, perform extract min, effectively removing the node.
"""

## 4. Common Use Cases

"""
Fibonacci Heaps are particularly useful in scenarios where decrease key operations are frequent. Common use cases include:

- Implementing Dijkstra's algorithm for shortest paths, where the decrease key operation is extensively used.
- Prim's algorithm for finding the minimum spanning tree.
- Any application requiring a priority queue where the workload involves many decrease key operations.
"""

## 5. Trade-offs

"""
The primary trade-off with Fibonacci Heaps is between complexity and performance. While they offer excellent amortized 
time complexities, the actual constant factors can be high due to the structure's complexity. This makes Fibonacci Heaps 
less favorable in practice unless the specific use case can leverage the amortized benefits effectively.
"""

## 6. Design Decisions

"""
Fibonacci Heaps use a lazy approach to consolidate trees, delaying the actual organization until it becomes necessary. 
The decision to use a circular doubly linked list for roots allows efficient merging and traversal of the heap's top-level 
nodes. The mark mechanism and cascading cuts in the decrease key operation are designed to maintain balance while minimizing 
the restructuring effort.
"""

## 7. Visual / Intuition

"""
Visually, a Fibonacci Heap can be imagined as a collection of trees where the minimum value is easily accessible. When 
the minimum is removed, trees are consolidated to maintain the heap properties. This structure allows flexibility in 
how trees are maintained, focusing on delaying work until absolutely necessary.
"""

## 8. Programming Patterns

"""
The Fibonacci Heap introduces patterns such as lazy evaluation and amortized analysis to optimize performance. The structure 
leverages cut and consolidate operations to ensure key operations remain efficient over time. These patterns are useful in 
optimizing algorithms that require dynamic priority management.
"""

## 9. Typical Problems

"""
Problems that can be efficiently solved using Fibonacci Heaps often involve dynamic sets of priorities, such as:

- Network routing protocols requiring shortest path calculations.
- Dynamic graph algorithms where edge weights change frequently.
- Event-driven simulations where priorities of events need constant updating.
"""

## 10. Gotchas / Pitfalls

"""
Implementing Fibonacci Heaps can be complex and error-prone due to the intricate pointer management and the lazy consolidation 
strategy. Mismanagement of the mark and degree properties can lead to incorrect heap states. Additionally, while amortized 
complexity is favorable, real-world performance can be impacted by the high constant factors involved.
"""

## 11. Code Implementation (Demo of Core Operations)

class Node:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.mark = False
        self.parent = None
        self.child = None
        self.left = self
        self.right = self

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.total_nodes = 0

    def insert(self, key):
        node = Node(key)
        if not self.min_node:
            self.min_node = node
        else:
            self._add_to_root_list(node)
            if node.key < self.min_node.key:
                self.min_node = node
        self.total_nodes += 1
        return node

    def find_min(self):
        if not self.min_node:
            return None
        return self.min_node.key

    def union(self, other_heap):
        if not other_heap.min_node:
            return self
        if not self.min_node:
            self.min_node = other_heap.min_node
            self.total_nodes = other_heap.total_nodes
        else:
            self._concatenate_root_lists(other_heap)
            if other_heap.min_node.key < self.min_node.key:
                self.min_node = other_heap.min_node
            self.total_nodes += other_heap.total_nodes
        return self

    def extract_min(self):
        min_node = self.min_node
        if min_node:
            if min_node.child:
                self._add_children_to_root_list(min_node)
            self._remove_from_root_list(min_node)
            if min_node == min_node.right:
                self.min_node = None
            else:
                self.min_node = min_node.right
                self._consolidate()
            self.total_nodes -= 1
        return min_node.key if min_node else None

    def decrease_key(self, node, new_key):
        if new_key > node.key:
            raise ValueError("New key is greater than current key")
        node.key = new_key
        parent = node.parent
        if parent and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)
        if node.key < self.min_node.key:
            self.min_node = node

    def delete(self, node):
        self.decrease_key(node, float('-inf'))
        self.extract_min()

    # Helper methods for internal operations
    def _add_to_root_list(self, node):
        node.left = self.min_node
        node.right = self.min_node.right
        self.min_node.right.left = node
        self.min_node.right = node

    def _remove_from_root_list(self, node):
        node.left.right = node.right
        node.right.left = node.left

    def _concatenate_root_lists(self, other_heap):
        self.min_node.right.left = other_heap.min_node.left
        other_heap.min_node.left.right = self.min_node.right
        self.min_node.right = other_heap.min_node
        other_heap.min_node.left = self.min_node

    def _add_children_to_root_list(self, min_node):
        child = min_node.child
        if child:
            start = child
            while True:
                next_child = child.right
                self._add_to_root_list(child)
                child.parent = None
                child = next_child
                if child == start:
                    break

    def _consolidate(self):
        max_degree = int(self.total_nodes**0.5) + 1
        degree_table = [None] * max_degree

        nodes = []
        start = self.min_node
        if start:
            nodes.append(start)
            node = start.right
            while node != start:
                nodes.append(node)
                node = node.right

        for node in nodes:
            degree = node.degree
            while degree_table[degree]:
                other = degree_table[degree]
                if node.key > other.key:
                    node, other = other, node
                self._link(other, node)
                degree_table[degree] = None
                degree += 1
            degree_table[degree] = node

        self.min_node = None
        for node in degree_table:
            if node:
                if not self.min_node or node.key < self.min_node.key:
                    self.min_node = node

    def _link(self, child, parent):
        self._remove_from_root_list(child)
        child.left = child.right = child
        child.parent = parent
        if not parent.child:
            parent.child = child
        else:
            child.right = parent.child.right
            child.left = parent.child
            parent.child.right.left = child
            parent.child.right = child
        parent.degree += 1
        child.mark = False

    def _cut(self, node, parent):
        if node.right == node:
            parent.child = None
        else:
            node.left.right = node.right
            node.right.left = node.left
            if parent.child == node:
                parent.child = node.right
        parent.degree -= 1
        self._add_to_root_list(node)
        node.parent = None
        node.mark = False

    def _cascading_cut(self, node):
        parent = node.parent
        if parent:
            if not node.mark:
                node.mark = True
            else:
                self._cut(node, parent)
                self._cascading_cut(parent)
