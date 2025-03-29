# Skip List Data Structure

```python
```python
# Skip List Data Structure

## 1. Concept Overview

"""
A Skip List is a data structure that allows fast search, insertion, and deletion operations within an ordered sequence of elements. 
It is a probabilistic alternative to balanced trees and uses multiple layers of linked lists to achieve logarithmic time complexity on average. 
Each element in a skip list is represented by a node, and nodes are connected in such a way that there are multiple levels, where the bottom 
level is an ordinary ordered linked list and higher levels act as "express lanes" to skip over multiple nodes to speed up the search process.
"""

## 2. Implementation Details

"""
A Skip List consists of several layers. Each layer is a sorted linked list, and each list is a subset of the one below it. 
The bottom layer contains all the elements, and each upper layer acts as an express lane with fewer nodes. 
When searching for an element, the algorithm begins at the topmost list, moving horizontally until it finds a node greater than the target, 
then drops down a level and continues. This structure allows average time complexities of O(log n) for search, insertion, and deletion.

The probability factor 'p' determines how likely it is for an element to be inserted into an upper level. 
A common choice is p = 0.5, which results in logarithmic height with high probability.
"""

## 3. Core Operations & Time Complexities

"""
1. Search: O(log n) on average, as the search algorithm skips over nodes using higher-level lists.
2. Insert: O(log n) on average, since insertion may require re-linking nodes at multiple levels.
3. Delete: O(log n) on average, as it involves re-linking nodes similarly to the insertion process.
"""

## 4. Common Use Cases

"""
Skip Lists are ideal for use cases where balanced trees might be used, such as:
- Implementing ordered dictionaries or sets.
- Handling concurrent access in lock-free data structures.
- Use in distributed systems and databases for efficient range queries.
"""

## 5. Trade-offs

"""
Advantages:
- Simplicity and ease of implementation compared to balanced trees.
- Randomized balancing avoids worst-case scenarios typical with deterministic structures.

Disadvantages:
- Requires additional space for higher-level links.
- Randomization means performance guarantees are probabilistic rather than absolute.
"""

## 6. Design Decisions

"""
Design decisions include:
- The choice of the probability factor 'p', commonly set to 0.5 for balanced performance.
- The maximum number of levels, typically based on the logarithm of the number of elements.
- Whether to use sentinel nodes to simplify boundary conditions.
"""

## 7. Visual / Intuition

"""
Imagine a series of linked lists stacked on top of each other, where each higher list skips over more elements than the one below it.
Searching involves descending from the topmost list downwards, moving horizontally as far as possible at each level before dropping down.
"""

## 8. Programming Patterns

"""
Skip Lists often utilize:
- Probabilistic randomization to determine node levels.
- Layered design patterns to manage multiple levels of linked lists.
- Recursive or iterative patterns to traverse lists efficiently.
"""

## 9. Typical Problems

"""
- Implementing efficient search, insert, and delete operations.
- Maintaining the probabilistic balance across all levels.
- Ensuring space efficiency with the chosen probability factor.
"""

## 10. Gotchas / Pitfalls

"""
- Mismanagement of random level generation can lead to inefficiencies.
- Edge cases in linking nodes between levels need careful handling.
- Overestimating the height can lead to unnecessary space usage.
"""

## 11. Code Implementation (Demo of Core Operations)

import random

class Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level, p):
        self.max_level = max_level
        self.p = p
        self.header = self._create_node(self.max_level, None)
        self.level = 0

    def _create_node(self, lvl, value):
        return Node(value, lvl)

    def _random_level(self):
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def insert(self, value):
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current is None or current.value != value:
            random_level = self._random_level()

            if random_level > self.level:
                for i in range(self.level + 1, random_level + 1):
                    update[i] = self.header
                self.level = random_level

            new_node = self._create_node(random_level, value)

            for i in range(random_level + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def search(self, value):
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]

        current = current.forward[0]
        return current and current.value == value

    def delete(self, value):
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current and current.value == value:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1

# Example usage
skiplist = SkipList(3, 0.5)
skiplist.insert(3)
skiplist.insert(6)
skiplist.insert(7)
skiplist.insert(9)
skiplist.insert(12)
skiplist.insert(19)
print("Search 7:", skiplist.search(7))  # Output: True
print("Search 15:", skiplist.search(15))  # Output: False
skiplist.delete(3)
print("Search 3:", skiplist.search(3))  # Output: False
```
```