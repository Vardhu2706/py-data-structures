# Patricia Trie Data Structure

```python
```python
# Patricia Trie Data Structure

## 1. Concept Overview

"""
A Patricia Trie, or Practical Algorithm to Retrieve Information Coded in Alphanumeric, is a specialized form of a Trie data structure. It is used to store a set of strings in a compressed manner, making it efficient for both space and search operations. Unlike a standard Trie, a Patricia Trie compresses chains of single-child nodes by combining them into a single edge with a label. This reduces the height of the tree and improves the search time complexity. Patricia Tries are particularly useful in applications where space is a constraint, such as IP routing tables and dictionary implementations.
"""

## 2. Implementation Details

"""
In a Patricia Trie, each node can have multiple children and each edge is labeled with a string. The main operations are insertion, deletion, and search. During insertion, common prefixes are shared, and the trie is compressed by merging nodes with only one child. Deletion involves removing nodes and potentially merging paths to maintain the compressed structure. The search operation benefits from the trie’s compact representation by following labeled edges to match the input query.
"""

## 3. Core Operations & Time Complexities

"""
1. Insertion: O(L) - where L is the length of the string being inserted. In a Patricia Trie, insertion involves traversing the trie to find the correct position, then potentially splitting an edge if necessary.

2. Deletion: O(L) - where L is the length of the string being deleted. Deletion may require merging paths if nodes become redundant.

3. Search: O(L) - where L is the length of the query string. The search operation traverses the trie according to the edge labels.

4. Space Complexity: O(N) - where N is the total number of characters in all strings stored in the trie. The compression in Patricia Tries helps reduce the space usage compared to a standard trie.
"""

## 4. Common Use Cases

"""
- IP Routing Tables: Patricia Tries are used to store IP prefixes efficiently for fast routing lookups.
- String Matching: Used in applications that require frequent substring searches.
- Dictionary Implementations: For storing large sets of words in a compact way.
- Autocomplete Engines: Efficiently suggest completions for a given prefix.
"""

## 5. Trade-offs

"""
- Pros: Improved space efficiency over standard tries due to path compression; relatively simple to implement and manage.
- Cons: More complex than standard tries; each operation involves handling string splits and merges which can be error-prone.
"""

## 6. Design Decisions

"""
- Path Compression: By compressing paths in the trie, the Patricia Trie minimizes the number of nodes, which reduces memory usage and potentially speeds up operations.
- Edge Labeling: Instead of nodes containing single characters, edges are labeled with strings, allowing for more compact representation.
- Balancing Act: While the data structure is more space-efficient, the additional complexity in managing edge labels and splits must be carefully handled to maintain performance.
"""

## 7. Visual / Intuition

"""
Imagine a standard Trie where each node has only one child for long chains of characters. A Patricia Trie takes these chains and compresses them into a single edge with a label. This way, searching for a string involves fewer steps as long paths are reduced to single labeled edges.
"""

## 8. Programming Patterns

"""
- Recursive Traversal: Operations like insertion and search can be implemented recursively to traverse the trie efficiently.
- Edge Splitting: During insertion, if a mismatch occurs partway through an edge label, the edge must be split and a new node created.
- Path Merging: During deletion, if removing a string causes a node to have only one child, paths should be merged to maintain the compressed structure.
"""

## 9. Typical Problems

"""
- Implementing an efficient IP routing table using a Patricia Trie.
- Developing an autocomplete feature for a search engine using Patricia Tries.
- Designing a memory-efficient dictionary for large datasets.
"""

## 10. Gotchas / Pitfalls

"""
- Edge Cases in Edge Splitting: Care must be taken to handle edge label splits correctly when inserting new strings.
- Maintaining Compression: Ensuring that the trie remains compressed after insertion and deletion operations is crucial for performance.
- Complexity in Deletion: Properly merging paths and handling node removal can be more complex than in a standard Trie.
"""

## 11. Code Implementation (Demo of Core Operations)

class PatriciaTrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class PatriciaTrie:
    def __init__(self):
        self.root = PatriciaTrieNode()

    def insert(self, word):
        current = self.root
        index = 0
        while index < len(word):
            char = word[index]
            if char not in current.children:
                current.children[char] = PatriciaTrieNode()
            current = current.children[char]
            index += 1
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        index = 0
        while index < len(word):
            char = word[index]
            if char not in current.children:
                return False
            current = current.children[char]
            index += 1
        return current.is_end_of_word

    def delete(self, word):
        def _delete(current, word, index):
            if index == len(word):
                if not current.is_end_of_word:
                    return False
                current.is_end_of_word = False
                return len(current.children) == 0
            char = word[index]
            if char not in current.children:
                return False
            can_delete = _delete(current.children[char], word, index + 1)
            if can_delete:
                del current.children[char]
                return len(current.children) == 0 and not current.is_end_of_word
            return False

        _delete(self.root, word, 0)
```
```