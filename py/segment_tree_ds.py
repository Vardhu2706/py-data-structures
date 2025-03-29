# Segment Tree Data Structure

## 1. Concept Overview

"""
A Segment Tree is a versatile data structure that allows for efficient querying and updating of elements in a range of an array. It is particularly useful for scenarios where array elements are frequently modified, and queries regarding cumulative information of segments (such as sum, minimum, maximum, greatest common divisor, etc.) are required.

The Segment Tree is essentially a binary tree where each node represents a segment (or range) of the array. The leaf nodes correspond to individual elements of the array, and the internal nodes store information about a segment of the array determined by combining the information of their child nodes.

The principal advantage of a Segment Tree is its ability to perform both update and query operations in logarithmic time complexity, O(log n), which is a significant improvement over the naive O(n) approach for each operation.
"""

## 2. Implementation Details

"""
A Segment Tree is usually implemented as an array-based binary tree. For an array `arr` of length `n`, a Segment Tree typically requires an array of size `2 * 2^ceil(log2(n)) - 1` to store the nodes. This ensures that there is enough space to store the complete binary tree representation.

The tree is built recursively:
- The root node represents the whole array.
- Each internal node represents a segment of the array, and this is divided into two halves, managed by its left and right children.

The tree supports two main operations:
1. Build (or Initialize): Construct the tree from the input array.
2. Query: Retrieve information for a given range.
3. Update: Modify the value of an element and propagate the changes through the tree.
"""

## 3. Core Operations & Time Complexities

"""
1. Build Segment Tree:
   - Time Complexity: O(n), where `n` is the number of elements in the array.
   - The tree is built from the bottom up, and each node is computed as the combination (such as sum or min) of its two children.

2. Range Query:
   - Time Complexity: O(log n).
   - The query operation fetches information from the relevant segments of the tree, which involves traversing from the root to the leaves, similar to a binary search.

3. Update Element:
   - Time Complexity: O(log n).
   - The update operation alters the value of an element and updates all relevant nodes in the tree to reflect this change.
"""

## 4. Common Use Cases

"""
- Range Sum Queries: Efficiently compute the sum of elements in a specific range of an array.
- Range Minimum/Maximum Queries: Find the minimum or maximum in a segment of an array.
- Range GCD Queries: Compute the greatest common divisor of all elements in a segment.
- Dynamic Programming Optimization: Used in scenarios where states can be represented by segments.
- Problems involving interval updates and queries.
"""

## 5. Trade-offs

"""
- Memory Usage: Segment Trees require additional space, approximately 4 times the size of the input array, to store the tree structure.
- Complexity in Implementation: Implementing a Segment Tree is more complex than simpler data structures like arrays or lists.
- Static Range Size: Although efficient, the Segment Tree is less flexible when the range size or number of elements changes frequently.
"""

## 6. Design Decisions

"""
- Node Representation: The choice of operation for combining nodes (e.g., sum, min, max) depends on the problem requirements.
- Lazy Propagation: For certain types of range updates, a technique called lazy propagation can be used to delay updates, optimizing the time complexity for multiple updates.
- Dynamic Segment Trees: For very large element ranges, a dynamic version of the Segment Tree can be used, which allocates nodes only when needed.
"""

## 7. Visual / Intuition

"""
Visually, a Segment Tree resembles a complete binary tree:
- The root node covers the entire array.
- Each level of the tree represents increasingly smaller segments of the array.
- Leaf nodes represent individual elements, while internal nodes combine information from their children to represent segments.
"""

## 8. Programming Patterns

"""
- Divide and Conquer: The Segment Tree leverages the divide and conquer methodology by recursively breaking down the problem into smaller segments.
- Tree Traversal: Operations on the Segment Tree often involve a form of depth-first search (DFS) to traverse from the root to leaves and back.
"""

## 9. Typical Problems

"""
- Range Sum Queries
- Range Minimum/Maximum Queries
- Dynamic Range GCD Queries
- Interval Add/Update with Range Queries
- 2D Segment Trees for matrix-like problems
"""

## 10. Gotchas / Pitfalls

"""
- Off-by-One Errors: Care must be taken in correctly managing indices, especially in zero-based indexing systems.
- Initialization: The tree must be initialized properly, ensuring all nodes are correctly set based on their children.
- Lazy Propagation Complexity: Implementing lazy propagation requires careful management of deferred updates.
"""

## 11. Code Implementation (Demo of Core Operations)

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(data, 0, 0, self.n - 1)

    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(data, left_child, start, mid)
            self.build(data, right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, idx, value, node, start, end):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if start <= idx <= mid:
                self.update(idx, value, left_child, start, mid)
            else:
                self.update(idx, value, right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, L, R, node, start, end):
        if R < start or end < L:
            return 0
        if L <= start and end <= R:
            return self.tree[node]
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_sum = self.query(L, R, left_child, start, mid)
        right_sum = self.query(L, R, right_child, mid + 1, end)
        return left_sum + right_sum

# Example Usage
data = [1, 3, 5, 7, 9, 11]
segment_tree = SegmentTree(data)
print("Initial range sum (0, 3):", segment_tree.query(0, 3, 0, 0, len(data) - 1))
segment_tree.update(1, 10, 0, 0, len(data) - 1)
print("Updated range sum (0, 3):", segment_tree.query(0, 3, 0, 0, len(data) - 1))
