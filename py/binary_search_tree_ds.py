# Binary Search Tree Data Structure

## 1. Concept Overview

"""
A Binary Search Tree (BST) is a node-based binary tree data structure with the following properties:
- Each node has a maximum of two children, referred to as the left child and the right child.
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- There must be no duplicate nodes.

BSTs are used to implement dynamic sets and lookup tables. The key advantage of a BST is its ability to maintain a sorted sequence of elements, allowing for fast search, insertion, and deletion operations.
"""

## 2. Implementation Details

"""
A typical binary search tree is implemented with a class for the tree itself and a class for its nodes. Each node contains:
- A key or value.
- Pointers to the left and right children.
- (Optional) A pointer to the parent node, which can be useful for certain operations.

The tree class typically contains methods for:
- Inserting a new key.
- Deleting a key.
- Searching for a key.
- Traversing the tree (in-order, pre-order, post-order).
- Finding the minimum and maximum keys.
"""

## 3. Core Operations & Time Complexities

"""
1. Search: O(h) average and worst case, where h is the height of the tree.
2. Insert: O(h) average and worst case.
3. Delete: O(h) average and worst case.
4. In-order Traversal: O(n), where n is the number of nodes.
5. Minimum/Maximum: O(h), where h is the height of the tree.

For a balanced BST, the height h is O(log n), making these operations efficient. However, in the worst case of an unbalanced tree, h can be O(n).
"""

## 4. Common Use Cases

"""
- Implementing associative arrays or dictionaries.
- Indexing for databases.
- Maintaining a sorted list of numbers.
- Priority queues and scheduling.
"""

## 5. Trade-offs

"""
- BSTs provide fast search, insert, and delete operations on average but can degrade to O(n) time complexity if the tree becomes unbalanced.
- They require additional space for pointers as compared to an array-based structure.
- Balancing a BST, such as using AVL or Red-Black Trees, can introduce overhead.
"""

## 6. Design Decisions

"""
- Choosing whether or not to allow duplicate keys (usually not allowed in a strict BST).
- Deciding between iterative and recursive implementations.
- Whether to incorporate balancing mechanisms to maintain performance guarantees.
"""

## 7. Visual / Intuition

"""
Visualize a BST as a hierarchical structure with each node having up to two children. The left child contains smaller values, and the right child contains larger values. This property helps in efficiently narrowing down the search space by half at each step.
"""

## 8. Programming Patterns

"""
- Recursion is frequently used for traversal operations and can simplify the code.
- Iterative solutions may be preferred for non-recursive environments or to avoid stack overflow.
- When implementing delete operations, handling the three cases (leaf, one child, two children) is crucial.
"""

## 9. Typical Problems

"""
- Find kth smallest/largest element in BST.
- Convert sorted array to a balanced BST.
- Validate if a given binary tree is a BST.
- Find the lowest common ancestor (LCA) of two nodes.
"""

## 10. Gotchas / Pitfalls

"""
- Failing to handle the edge case of deleting nodes with two children correctly.
- Not maintaining the BST properties after insertion or deletion.
- Allowing the tree to become unbalanced, leading to degraded performance.
"""

## 11. Code Implementation (Demo of Core Operations)

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """ Inserts a key into the BST. """
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        """ Searches for a key in the BST. Returns True if found, else False. """
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        """ Deletes a key from the BST if it exists. """
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node with two children, get the inorder successor (smallest in the right subtree)
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        """ Returns the in-order traversal of the BST as a list. """
        traversal = []
        self._inorder_traversal(self.root, traversal)
        return traversal

    def _inorder_traversal(self, node, traversal):
        if node is not None:
            self._inorder_traversal(node.left, traversal)
            traversal.append(node.key)
            self._inorder_traversal(node.right, traversal)

# Example usage
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("In-order Traversal:", bst.inorder_traversal())
print("Search for 40:", bst.search(40))
print("Search for 100:", bst.search(100))

bst.delete(20)
print("In-order Traversal after deleting 20:", bst.inorder_traversal())

bst.delete(30)
print("In-order Traversal after deleting 30:", bst.inorder_traversal())

bst.delete(50)
print("In-order Traversal after deleting 50:", bst.inorder_traversal())

"""
This code demonstrates a basic implementation of a Binary Search Tree in Python, covering core operations such as insertion, search, and deletion. Each operation is designed to preserve BST properties, ensuring efficient data management.
"""
