# B-Tree Data Structure

## 1. Concept Overview

"""
A B-Tree is a self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time. It is a generalization of a binary search tree in that a node can have more than two children. B-Trees are primarily used in databases and file systems to allow quick access to large blocks of data.

Key characteristics of a B-Tree:
- Every node has at most `m` children where `m` is the order of the tree.
- Every node except the root must have at least `⌈m/2⌉` children.
- The root must have at least two children if it is not a leaf node.
- All leaves appear on the same level, thus ensuring the tree remains balanced.
- A non-leaf node with `k` children contains `k-1` keys.
"""

## 2. Implementation Details

"""
B-Trees consist of nodes that have a certain number of keys and child pointers. The keys within a node are stored in sorted order. Each key in a node acts as a separation value which separates the subtrees. The B-Tree dynamically adjusts its height by splitting and merging nodes as necessary to maintain the balance criteria.

A typical node in a B-Tree contains:
- A list of keys.
- A list of child pointers.
- A boolean indicating whether it's a leaf node.
- A maximum and minimum number of keys, dependent on the order of the tree.

When a node becomes full (i.e., reaches `m` keys), it splits into two nodes and the middle key is promoted to the parent node.
"""

## 3. Core Operations & Time Complexities

"""
- Search: O(log n)
- Insert: O(log n)
- Delete: O(log n)

The time complexities arise because the height of the B-Tree is logarithmic with respect to the number of keys. Each operation involves traversing down the tree, which takes logarithmic time, and possibly modifying nodes, which is also logarithmically bounded.
"""

## 4. Common Use Cases

"""
B-Trees are commonly used in:
- Database indexing: They are used to store keys in a database to allow quick retrieval of records.
- File systems: They organize directories and files efficiently, allowing quick access and modification.
- Multilevel indexing: B-Trees are used for efficient, scalable indexing in memory and storage systems.
"""

## 5. Trade-offs

"""
- Pros:
  - Efficient use of disk space and memory, as nodes are kept partially full.
  - Balanced tree structure ensures consistent performance.
  - Supports a large number of keys and child nodes, making it suitable for large datasets.

- Cons:
  - Complexity in implementation compared to simpler structures like binary search trees.
  - Overhead of maintaining balance can affect performance for small datasets.
"""

## 6. Design Decisions

"""
Key design decisions for implementing a B-Tree include:
- Choosing the order `m` of the tree, which affects how full nodes can be and how frequently nodes split.
- Handling underflows in nodes by merging or redistributing keys from sibling nodes.
- Deciding on the structure of the node (array or linked list) for storing keys and child pointers.
"""

## 7. Visual / Intuition

"""
Visualizing a B-Tree helps understand its structure:
- Imagine a tree where each node can have multiple children and keys.
- Nodes split and merge to maintain balance, with keys dividing the range of values between children.
- All leaf nodes are at the same depth, keeping the height of the tree minimal.
"""

## 8. Programming Patterns

"""
Programming patterns for B-Trees often involve recursive functions for insertion, deletion, and searching:
- Recursive descent through the tree to the appropriate child for operations.
- Handling special cases for root and leaf nodes separately.
- Using split and merge operations to maintain tree balance.
"""

## 9. Typical Problems

"""
- Implementing a B-Tree from scratch requires careful handling of edge cases like node overflow and underflow.
- Choosing an optimal order `m` for the tree based on expected data size and access patterns.
- Balancing time complexity with space efficiency for different types of applications.
"""

## 10. Gotchas / Pitfalls

"""
- Forgetting to handle the special case where the root node is the only node and becomes empty.
- Incorrectly implementing key redistributions between sibling nodes, leading to unbalanced trees.
- Overlooking the need to update parent pointers during node splits and merges.
"""

## 11. Code Implementation (Demo of Core Operations)

class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree (defines the range for number of keys)
        self.keys = []
        self.children = []
        self.leaf = leaf

    def insert_non_full(self, key):
        i = len(self.keys) - 1
        if self.leaf:
            # Insert the new key at the correct location in the leaf node
            self.keys.append(None)
            while i >= 0 and self.keys[i] > key:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:
            # Find the child that will have the new key
            while i >= 0 and self.keys[i] > key:
                i -= 1
            if len(self.children[i + 1].keys) == (2 * self.t) - 1:
                # If the child is full, split it
                self.split_child(i + 1, self.children[i + 1])
                if self.keys[i + 1] < key:
                    i += 1
            self.children[i + 1].insert_non_full(key)

    def split_child(self, i, y):
        t = self.t
        z = BTreeNode(t, y.leaf)
        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys[t - 1])

        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:(t - 1)]

        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]

    def traverse(self):
        i = 0
        for i in range(len(self.keys)):
            if not self.leaf:
                self.children[i].traverse()
            print(self.keys[i], end=' ')
        if not self.leaf:
            self.children[i].traverse()

    def search(self, key):
        i = 0
        while i < len(self.keys) and key > self.keys[i]:
            i += 1
        if i < len(self.keys) and self.keys[i] == key:
            return self
        if self.leaf:
            return None
        return self.children[i].search(key)


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def traverse(self):
        if self.root:
            self.root.traverse()

    def search(self, key):
        if self.root:
            return self.root.search(key)
        return None

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode(self.t)
            self.root = temp
            temp.children.insert(0, root)
            temp.split_child(0, root)
            temp.insert_non_full(key)
        else:
            root.insert_non_full(key)

# Example usage:
# btree = BTree(3)
# btree.insert(10)
# btree.insert(20)
# btree.insert(5)
# btree.insert(6)
# btree.insert(12)
# btree.insert(30)
# btree.insert(7)
# btree.insert(17)
# btree.traverse()
# print("\nSearch for 6:", btree.search(6) is not None)
"""
The above code implements a simple B-Tree with basic functionality for insertion, traversal, and searching. It demonstrates how nodes are split and keys are managed to maintain the properties of a B-Tree.
"""
