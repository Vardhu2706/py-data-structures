# Red-Black Tree Data Structure

## 1. Concept Overview

"""
A Red-Black Tree is a type of self-balancing binary search tree. Each node in the tree has an extra attribute: a color,
which is either red or black. The tree satisfies the following properties:
1. Each node is either red or black.
2. The root is black.
3. All leaves (NIL nodes) are black.
4. If a node is red, then both its children must be black (no two red nodes can be adjacent).
5. Every path from a node to its descendant NIL nodes must have the same number of black nodes.

These properties ensure that the tree remains approximately balanced, ensuring that the longest path from the root to a leaf
is no more than twice the length of the shortest path, thereby guaranteeing O(log n) time complexity for search, insert, and delete operations.
"""

## 2. Implementation Details

"""
A Red-Black Tree is usually implemented with nodes containing pointers to their parent and children, as well as a color attribute.
The NIL nodes are often represented by a single sentinel node to reduce the number of checks in the code.

Key operations like insertion and deletion require additional steps to maintain the tree's properties, often involving rotations
and recoloring of nodes.
"""

## 3. Core Operations & Time Complexities

"""
- Search: O(log n)
- Insert: O(log n) — Involves standard BST insert followed by fix-up operations to maintain properties.
- Delete: O(log n) — Involves standard BST delete followed by fix-up operations to maintain properties.
- Rotate: O(1) — Used internally during insert and delete fix-ups to maintain tree balance.
"""

## 4. Common Use Cases

"""
Red-Black Trees are used in environments where frequent insertions and deletions are expected, and balanced tree performance is required.
They are commonly used in:
- Implementations of associative arrays.
- The Linux kernel uses them in various subsystems.
- Java's TreeMap and C++'s map and multimap are typically implemented using Red-Black Trees.
"""

## 5. Trade-offs

"""
Advantages:
- Provides O(log n) time complexity for search, insert, and delete operations.
- The tree remains balanced without requiring O(n) operations.

Disadvantages:
- Slightly more complex to implement compared to AVL trees.
- Can have slightly slower read operations compared to AVL trees due to less strict balancing.
"""

## 6. Design Decisions

"""
The key design decision in Red-Black Trees is to use colors and the described properties to maintain a balanced tree.
The choice of rotations and recoloring during insertions and deletions ensures that the operations remain efficient while keeping
the tree balanced.
"""

## 7. Visual / Intuition

"""
Visualizing a Red-Black Tree helps to understand the balancing properties. Each red node must have black children, preventing
long consecutive sequences of red nodes, which aids in maintaining balance.

Consider drawing a tree where root and leaves are black, and internal red nodes have black children. This visual can help
to intuitively understand the balancing mechanism.
"""

## 8. Programming Patterns

"""
- Use of a sentinel NIL node to represent all leaf nodes simplifies code by reducing the need for null checks.
- Recursive or iterative implementation of tree traversal, insert, and delete operations.
- Use of helper functions for left and right rotations and fix-up procedures.
"""

## 9. Typical Problems

"""
- Implementing insertion and ensuring the tree remains balanced through rotations and recoloring.
- Implementing deletion, which is more complex than insertion due to the need to balance the tree post-deletion.
- Maintaining correct parent, child, and color pointers during complex operations.
"""

## 10. Gotchas / Pitfalls

"""
- Forgetting to update parent pointers during rotation.
- Incorrectly handling the NIL sentinel node.
- Failing to recolor nodes correctly during insert or delete fix-up operations.
"""

## 11. Code Implementation (Demo of Core Operations)

class RedBlackNode:
    def __init__(self, key, color, left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

class RedBlackTree:
    def __init__(self):
        self.NIL = RedBlackNode(key=None, color='black')
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, key):
        node = RedBlackNode(key=key, color='red', left=self.NIL, right=self.NIL)
        y = None
        x = self.root
        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        self.insert_fixup(node)

    def insert_fixup(self, node):
        while node.parent and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':  # Case 1
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:  # Case 2
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'black'  # Case 3
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'black'

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, key):
        z = self.search(self.root, key)
        if z is None:
            return
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'black':
            self.delete_fixup(x)

    def delete_fixup(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == 'red':
                    sibling.color = 'black'
                    x.parent.color = 'red'
                    self.left_rotate(x.parent)
                    sibling = x.parent.right
                if sibling.left.color == 'black' and sibling.right.color == 'black':
                    sibling.color = 'red'
                    x = x.parent
                else:
                    if sibling.right.color == 'black':
                        sibling.left.color = 'black'
                        sibling.color = 'red'
                        self.right_rotate(sibling)
                        sibling = x.parent.right
                    sibling.color = x.parent.color
                    x.parent.color = 'black'
                    sibling.right.color = 'black'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == 'red':
                    sibling.color = 'black'
                    x.parent.color = 'red'
                    self.right_rotate(x.parent)
                    sibling = x.parent.left
                if sibling.right.color == 'black' and sibling.left.color == 'black':
                    sibling.color = 'red'
                    x = x.parent
                else:
                    if sibling.left.color == 'black':
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        self.left_rotate(sibling)
                        sibling = x.parent.left
                    sibling.color = x.parent.color
                    x.parent.color = 'black'
                    sibling.left.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'black'

    def search(self, node, key):
        while node != self.NIL and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node
