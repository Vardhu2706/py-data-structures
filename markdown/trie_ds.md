# Trie Data Structure

```python
```python
# Trie Data Structure

## 1. Concept Overview

"""
A Trie, also known as a prefix tree, is a tree-like data structure that stores a dynamic set of strings, where the keys are usually strings. Unlike a binary search tree, no node in the tree stores the key associated with that node; instead, its position in the tree defines the key with which it is associated. All descendants of a node have a common prefix of the string associated with that node, and the root is associated with the empty string.

Tries are particularly useful for implementing dictionaries with predictive search functionalities, auto-completion, and spell-checking. They offer efficient searching with a time complexity of O(L), where L is the length of the key.
"""

## 2. Implementation Details

"""
A Trie is implemented using nodes that store an array or dictionary of children nodes. Each node corresponds to a single character of the key. The root node is an empty node, and paths from the root represent the keys stored in the Trie. Each node has:
- A boolean flag to indicate if it marks the end of a valid string.
- References to child nodes, typically in the form of a dictionary where keys are characters and values are the child nodes.
"""

## 3. Core Operations & Time Complexities

"""
1. Insertion: Add a word to the Trie.
   - Time Complexity: O(L), where L is the length of the word.
   
2. Search: Check if a word is present in the Trie.
   - Time Complexity: O(L), where L is the length of the word.
   
3. StartsWith: Check if there is any word in the Trie that starts with a given prefix.
   - Time Complexity: O(L), where L is the length of the prefix.
   
4. Deletion (optional): Remove a word from the Trie.
   - Time Complexity: O(L), where L is the length of the word.
"""

## 4. Common Use Cases

"""
- Auto-complete suggestions in search engines.
- Spell checking and correction tools.
- IP routing (Longest Prefix Matching).
- Implementing dictionary-based algorithms such as T9 predictive text.
- Storing a large number of words for quick retrieval.
"""

## 5. Trade-offs

"""
- Tries can consume a lot of memory, especially if the alphabet size is large, due to storing a potentially large number of pointers.
- Tries provide fast search, insert, and prefix operations, but this requires additional memory compared to other data structures like hash tables.
- In scenarios with a small dataset or short keys, a Trie may not be as efficient or necessary.
"""

## 6. Design Decisions

"""
- Choosing between an array or a dictionary for storing child nodes.
  - Arrays are more memory efficient if the alphabet size is small and fixed.
  - Dictionaries are space-saving when dealing with sparse data or large alphabets.
- Deciding how to handle case sensitivity and character encoding.
- Implementing optional operations like deletion based on use case requirements.
"""

## 7. Visual / Intuition

"""
Consider a Trie storing the words: "cat", "car", and "dog". The root node is empty. The 'c' node branches into two children: 'a' followed by 't' and 'r', indicating the words 'cat' and 'car'. Similarly, 'd' leads to 'o' and 'g' for the word 'dog'. Each path from the root to a node marked as the end of a word represents a valid word in the Trie.
"""

## 8. Programming Patterns

"""
- Recursive and iterative traversal for insertion and search.
- Use of backtracking for operations like deletion.
- Breadth-first and depth-first strategies for exploring nodes.
"""

## 9. Typical Problems

"""
- Implementing a Trie with insert, search, and startsWith operations.
- Designing a system for auto-suggestions using Tries.
- Finding the longest prefix match for a given string.
"""

## 10. Gotchas / Pitfalls

"""
- Memory usage can grow significantly with the number of words, especially with large alphabets.
- Deletion must be handled carefully to avoid removing nodes that are prefixes for other words.
- Not considering edge cases like empty strings or very long strings.
"""

## 11. Code Implementation (Demo of Core Operations)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True

# Example Usage
trie = Trie()
trie.insert("cat")
trie.insert("car")
trie.insert("dog")

assert trie.search("cat") == True
assert trie.search("car") == True
assert trie.search("dog") == True
assert trie.search("cow") == False
assert trie.startsWith("ca") == True
assert trie.startsWith("do") == True
assert trie.startsWith("co") == False
```
```