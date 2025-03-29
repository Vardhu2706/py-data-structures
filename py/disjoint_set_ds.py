# Disjoint Set Data Structure

## 1. Concept Overview

"""
The Disjoint Set, also known as Union-Find, is a data structure that keeps track of a set of elements partitioned into non-overlapping subsets. It supports two primary operations:
- Find: Determines which subset a particular element is in. This can be used for checking if two elements are in the same subset.
- Union: Merges two subsets into a single subset.

This data structure is particularly useful in scenarios where we need to manage and merge sets dynamically, such as in network connectivity, image processing, and Kruskal's algorithm for finding the minimum spanning tree of a graph.
"""

## 2. Implementation Details

"""
The Disjoint Set is typically implemented using two techniques to optimize the operations:
- Path Compression: A technique used in the Find operation to flatten the structure of the tree whenever Find is called. This keeps the tree flat, ensuring that future operations are faster.
- Union by Rank: A technique used in the Union operation to attach the smaller tree under the root of the larger tree, keeping the overall tree as shallow as possible.

The Disjoint Set is usually represented as a forest of trees, where each tree represents a subset.
"""

## 3. Core Operations & Time Complexities

"""
The core operations and their time complexities are:
- Find: O(α(n)) amortized time, where α is the inverse Ackermann function, which grows very slowly. Practically constant time.
- Union: O(α(n)) amortized time.

The combination of path compression and union by rank ensures that the operations are very efficient, even for large datasets.
"""

## 4. Common Use Cases

"""
Disjoint Sets are commonly used in:
- Network connectivity: To determine the connected components of a network.
- Kruskal's algorithm: To find the minimum spanning tree of a graph.
- Image processing: To label connected components.
- Percolation theory: To model systems that are composed of interconnected sites.
"""

## 5. Trade-offs

"""
The primary trade-off in using Disjoint Sets involves balancing the complexity of operations with the memory overhead. While the operations are very efficient, they require auxiliary arrays to keep track of parent pointers and rank information, which can increase memory usage.
"""

## 6. Design Decisions

"""
Key design decisions include:
- Utilizing path compression and union by rank to optimize operations.
- Choosing the appropriate data structures (arrays or lists) to efficiently manage disjoint sets.
- Deciding when to apply path compression, typically during the Find operation, to maintain efficiency.
"""

## 7. Visual / Intuition

"""
Visualize each subset as a tree, where each node points to its parent. Initially, each element is its own parent. As Unions occur, trees combine, with one root becoming the parent of another. Path compression reduces the height of these trees by making nodes point directly to the root, speeding up future operations.
"""

## 8. Programming Patterns

"""
A common pattern when using Disjoint Sets is:
1. Initialize each element as its own set.
2. Perform Unions as needed.
3. Use Find to check connectivity or group membership.
This pattern is prevalent in algorithms that require dynamic connectivity checks.
"""

## 9. Typical Problems

"""
Typical problems that benefit from Disjoint Set include:
- Dynamic connectivity queries in a network.
- Finding connected components in a graph.
- Checking if adding an edge creates a cycle in a graph.
- Implementing Kruskal's algorithm for minimum spanning trees.
"""

## 10. Gotchas / Pitfalls

"""
- Failing to apply path compression can lead to inefficient Find operations.
- Incorrect implementation of union by rank may lead to unnecessarily deep trees.
- Not handling elements outside the initialized range can lead to incorrect results or errors.
"""

## 11. Code Implementation (Demo of Core Operations)

class DisjointSet:
    def __init__(self, n):
        """ Initialize the Disjoint Set with `n` elements. """
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        """ Find the representative of the set containing `u`. Apply path compression. """
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        """ Union the sets containing `u` and `v`. Apply union by rank. """
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Example usage:
# Initialize a disjoint set with 5 elements
ds = DisjointSet(5)
ds.union(0, 1)
ds.union(1, 2)
print(ds.find(0) == ds.find(2))  # Output: True
print(ds.find(0) == ds.find(3))  # Output: False
