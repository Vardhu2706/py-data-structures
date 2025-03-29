# Fenwick Tree Data Structure

## 1. Concept Overview

"""
A Fenwick Tree, also known as a Binary Indexed Tree (BIT), is a data structure that provides efficient methods 
for cumulative frequency tables or prefix sums. It supports the following operations in logarithmic time:
- Point updates: Update the value at a specific index.
- Prefix sum queries: Calculate the cumulative sum of elements up to a given index.

The Fenwick Tree is particularly useful when dealing with scenarios that require dynamic cumulative frequency 
tables, as it allows both updates and queries to be performed in O(log n) time, where n is the number of elements.
"""

## 2. Implementation Details

"""
The Fenwick Tree is implemented using a 1-based index array, where each element in the array is responsible for 
maintaining the sum of a specific range of elements. The range covered by each element is determined by the 
least significant bit (LSB) of its index.

The update operation involves adding a value to an index and propagating this change up the tree, while the 
query operation accumulates sums by traversing downward using the LSB to determine the next index to include 
in the sum.
"""

## 3. Core Operations & Time Complexities

"""
- Update(index, delta): O(log n)
  Updates the element at the specified index by a given delta value and propagates the change through the tree.

- Query(index): O(log n)
  Returns the cumulative sum of elements from the start of the array up to the specified index.

- RangeQuery(left, right): O(log n)
  Computes the sum of elements within a specific range by utilizing two prefix sum queries.
"""

## 4. Common Use Cases

"""
- Dynamic cumulative frequency tables.
- Inversion count problems.
- Range sum queries with point updates.
- Efficient handling of prefix sums in scenarios with frequent updates.
"""

## 5. Trade-offs

"""
- Fenwick Trees provide efficient updates and prefix sum queries, but they do not support dynamic resizing well.
- While they are great for point updates, they are less efficient than segment trees for arbitrary range updates.
"""

## 6. Design Decisions

"""
- The choice of using a 1-based index simplifies the computation for determining parent and child nodes using bit 
  manipulation.
- The representation of the tree is compact, requiring only an auxiliary array of the same size as the input data.
"""

## 7. Visual / Intuition

"""
Visualize the Fenwick Tree as a binary tree where each node at index i aggregates the sum of elements from 
index i - 2^k + 1 to i, where k is the position of the least significant set bit in i. This means each node 
covers a specific range of its predecessors, allowing efficient accumulation of prefix sums.
"""

## 8. Programming Patterns

"""
- Bit Manipulation: Use of bitwise operations to navigate tree indices (e.g., `i += i & -i` for updates).
- Cumulative Sums: Efficiently calculate prefix sums for arrays with frequent updates.
"""

## 9. Typical Problems

"""
- Range sum queries with point updates.
- Number of inversions in an array.
- Finding prefix sums in a dynamic array.
"""

## 10. Gotchas / Pitfalls

"""
- Remember that Fenwick Trees use 1-based indexing.
- Ensure the array is properly initialized; otherwise, queries may return incorrect results.
- Be cautious with the range of indices during updates and queries to avoid out-of-bounds errors.
"""

## 11. Code Implementation (Demo of Core Operations)

class FenwickTree:
    def __init__(self, size):
        """Initializes a Fenwick Tree for a given size."""
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        """Updates the element at index by delta."""
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        """Returns the prefix sum from the start to the given index."""
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

    def range_query(self, left, right):
        """Returns the sum of elements within the range [left, right]."""
        return self.query(right) - self.query(left - 1)

# Example Usage:
# Initialize a Fenwick Tree with 10 elements
fenwick_tree = FenwickTree(10)

# Update index 3 by 5
fenwick_tree.update(3, 5)

# Get prefix sum up to index 5
print(fenwick_tree.query(5))  # Output: 5

# Get range sum from index 3 to 5
print(fenwick_tree.range_query(3, 5))  # Output: 5
