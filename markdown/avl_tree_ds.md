# AVL Tree Data Structure

```python
```python
# AVL Tree Data Structure

## 1. Concept Overview

"""
An AVL Tree is a self-balancing binary search tree where the difference between heights of left and right subtrees 
cannot be more than one for all nodes. Named after its inventors Adelson-Velsky and Landis, it maintains O(log n) 
time complexity for search, insertion, and deletion operations by ensuring the tree remains balanced at all times.
"""

## 2. Implementation Details

"""
The AVL Tree maintains balance through rotations during insertions and deletions. Each node in the AVL Tree 
maintains an additional field called balance factor, which is the difference in heights between the left and right 
subtrees. There are four types of rotations used to maintain balance:
1. Right Rotation (Single Rotation)
2. Left Rotation (Single Rotation)
3. Left-Right Rotation (Double Rotation)
4. Right-Left Rotation (Double Rotation)

Balance factor of each node is calculated as:
    balance_factor = height(left_subtree) - height(right_subtree)

Rotations ensure the balance factor remains within the range [-1, 1].
"""

## 3. Core Operations & Time Complexities

"""
The core operations in an AVL Tree include:

1. Insertion: O(log n)
   - Inserts a new key while maintaining the balance of the tree using rotations if necessary.

2. Deletion: O(log n)
   - Deletes a key and rebalances the tree using rotations.

3. Search: O(log n)
   - Searches for a key in the tree.

4. Get Height: O(1)
   - Obtains the height of a node.

5. Get Balance: O(1)
   - Computes the balance factor of a node.
"""

## 4. Common Use Cases

"""
AVL Trees are used in applications requiring frequent insertions and deletions, and where the data needs to be 
retrieved in a sorted order. Common use cases include:
- Databases and Memory Management
- Priority Scheduling
- In-memory storage for fast lookups
"""

## 5. Trade-offs

"""
Pros:
- Guarantees O(log n) time complexity for insertions, deletions, and searches.
- Provides ordered data.
- Useful in scenarios where frequent modifications are required.

Cons:
- More complex to implement compared to simpler structures like binary search trees.
- Rotations increase the constant factors in time complexity.
- Might require more rotations compared to other balanced trees like Red-Black Trees.
"""

## 6. Design Decisions

"""
- The choice of AVL Tree over other balanced trees depends on the need for strict balancing, which AVL Trees provide.
- Rotations are chosen to keep the tree height minimal, ensuring efficient operations.
- Balance factors are used to decide when and which type of rotations are necessary.
"""

## 7. Visual / Intuition

"""
Visualize an AVL Tree as a binary search tree that 'self-corrects' to prevent skewing. 
Imagine balancing a set of scales where each node adjusts its position to ensure the entire tree remains level.
"""

## 8. Programming Patterns

"""
The recursive nature of AVL Tree operations (insertion, deletion) is crucial. Recursive functions handle 
rebalancing by traversing back up the tree to update heights and perform necessary rotations.
"""

## 9. Typical Problems

"""
- Implementing an AVL Tree from scratch.
- Modifying tree structures to maintain balance after insertions/deletions.
- Designing algorithms that leverage AVL Trees for efficient data processing.
"""

## 10. Gotchas / Pitfalls

"""
- Forgetting to update heights after rotations can disrupt the balance of the tree.
- Incorrect handling of double rotations can lead to incorrect tree structures.
- Overhead from rotations might not be justified for read-heavy applications.
"""

## 11. Code Implementation (Demo of Core Operations)

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def insert(self, node, key):
        if not node:
            return AVLNode(key)
        
        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.min_value_node(node.left)

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
```
```