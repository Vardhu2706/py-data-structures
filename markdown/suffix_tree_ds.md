# Suffix Tree Data Structure

```python
```python
# Suffix Tree Data Structure

## 1. Concept Overview

"""
A Suffix Tree is a compressed trie-like data structure that represents all the suffixes of a given string. It allows for efficient pattern matching and is used in various applications like substring search, pattern recognition, and bioinformatics. The Suffix Tree for a string of length n has at most n leaves and is constructed in O(n) time, making it extremely efficient for many string processing tasks. Each edge of the tree is labeled with a substring of the given string, and every suffix of the string corresponds to a unique path from the root to a leaf.
"""

## 2. Implementation Details

"""
The Suffix Tree is typically built using Ukkonen's algorithm, which is an online algorithm, meaning it processes the input string in a single pass. The tree consists of nodes and edges, where each edge is labeled with a substring of the input string. Internal nodes have at least two children, and leaves represent the end of suffixes. The tree is compacted, meaning long chains of nodes are represented by a single edge with an appropriate substring label.
"""

## 3. Core Operations & Time Complexities

"""
- Build Suffix Tree: O(n) time complexity using Ukkonen's algorithm.
- Search for a substring: O(m) time complexity, where m is the length of the substring.
- Longest Common Substring: O(n + m) time complexity, where n and m are the lengths of the two strings.
- Longest Repeated Substring: O(n) time complexity.
- Space Complexity: O(n), where n is the length of the input string.
"""

## 4. Common Use Cases

"""
- Fast substring search within a text.
- Finding the longest repeated substring in a string.
- Finding the longest common substring between two strings.
- Bioinformatics applications, such as genome sequencing and alignment.
- Data compression algorithms.
"""

## 5. Trade-offs

"""
- Suffix Trees require a large amount of memory, often 10 to 20 times the size of the input string.
- Construction is complex and requires thorough understanding of algorithms like Ukkonen's.
- While searching is efficient, the initial construction can be resource-intensive for very large strings.
"""

## 6. Design Decisions

"""
- Ukkonen's algorithm is chosen for its linear time complexity for construction.
- The tree is typically implemented using linked structures for nodes and edges to manage the dynamic nature of the tree efficiently.
- Edge labels are stored with start and end indices rather than substrings themselves to save space.
"""

## 7. Visual / Intuition

"""
Imagine a tree where each path from the root to a leaf represents a suffix of the string. Nodes branch whenever two suffixes diverge, and edges represent the substrings between these nodes. It's a compact representation that allows quick traversal and matching.
"""

## 8. Programming Patterns

"""
- Divide and Conquer: The structure divides the string into manageable suffixes.
- Online Algorithm: Processes input incrementally, useful for streaming data.
- Tree Traversal: Allows for efficient searching and pattern matching.
"""

## 9. Typical Problems

"""
- Constructing a Suffix Tree for a given string and performing substring searches.
- Finding the longest repeated substring in a string.
- Determining the longest common substring between two strings using generalized Suffix Trees.
"""

## 10. Gotchas / Pitfalls

"""
- Memory usage can be unexpectedly high due to the tree's size.
- Implementing Ukkonen's algorithm correctly is non-trivial and requires careful attention to detail.
- Edge cases such as strings with repeated patterns or very short strings can complicate construction.
"""

## 11. Code Implementation (Demo of Core Operations)

class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.start = -1
        self.end = -1
        self.suffix_link = None

class SuffixTree:
    def __init__(self, text):
        self.text = text
        self.root = SuffixTreeNode()
        self.build_suffix_tree()

    def build_suffix_tree(self):
        """
        Constructs the suffix tree using Ukkonen's algorithm.
        """
        # Implementation of Ukkonen's algorithm goes here.
        pass

    def search(self, pattern):
        """
        Searches for a substring in the suffix tree.
        Returns True if the pattern is found, otherwise False.
        """
        current_node = self.root
        i = 0
        while i < len(pattern):
            if pattern[i] in current_node.children:
                edge = current_node.children[pattern[i]]
                start_index = edge.start
                end_index = edge.end if edge.end != -1 else len(self.text)
                length = end_index - start_index
                substring = self.text[start_index:end_index]
                
                if pattern[i:i+length] == substring:
                    i += length
                    current_node = edge
                else:
                    return False
            else:
                return False
        return True

# Example usage
text = "bananas"
suffix_tree = SuffixTree(text)
print(suffix_tree.search("ana"))  # Expected output: True
print(suffix_tree.search("nana")) # Expected output: True
print(suffix_tree.search("apple")) # Expected output: False
```
```