# LRU Cache Data Structure

```python
```python
# LRU Cache Data Structure

## 1. Concept Overview

"""
The Least Recently Used (LRU) Cache is a data structure that stores a limited number of items 
and removes the least recently used item when the cache exceeds its capacity. This mechanism 
ensures that the most frequently accessed items remain available for quick retrieval, optimizing 
the cache's usefulness. The LRU Cache is commonly implemented using a combination of a doubly 
linked list and a hash map to provide O(1) time complexity for both insertion and retrieval operations.
"""

## 2. Implementation Details

"""
The LRU Cache requires two main components for efficient performance:
1. A doubly linked list to store the order of access, where the most recently used items are 
   moved to the front, and the least recently used items are at the back.
2. A hash map (or dictionary in Python) to allow O(1) access to the nodes in the linked list 
   to quickly update and remove nodes as necessary.

The combination of these structures allows the cache to maintain a fixed size while allowing 
constant time complexity for key operations like getting and setting cache entries.
"""

## 3. Core Operations & Time Complexities

"""
- `get(key)`: Returns the value associated with the key if it exists in the cache. It also 
  marks the item as recently used by moving it to the front of the list. This operation has 
  a time complexity of O(1).
  
- `put(key, value)`: Inserts a new key-value pair into the cache. If the key already exists, 
  it updates the value and marks the item as recently used. If the cache reaches its capacity, 
  it evicts the least recently used item before inserting the new key-value pair. This operation 
  also has a time complexity of O(1).
"""

## 4. Common Use Cases

"""
1. Memory Management: LRU Cache is used in operating systems and applications to manage 
   memory by keeping frequently accessed data readily available.
2. Web Caching: Used in web browsers and proxies to store recently accessed web pages or 
   resources, improving load times and reducing server requests.
3. Database Query Caching: Caches the results of frequent database queries to reduce 
   computation and improve response times.
"""

## 5. Trade-offs

"""
- Memory Overhead: The LRU Cache requires additional memory to maintain the doubly linked list 
  and hash map, which could be significant for large caches.
- Complexity: Implementing an LRU Cache correctly requires handling the interactions between 
  the linked list and hash map, which may introduce complexity in ensuring thread safety in 
  concurrent environments.
"""

## 6. Design Decisions

"""
- Doubly Linked List: Chosen for its ability to efficiently remove and insert nodes at both 
  ends, which is crucial for maintaining the order of usage in O(1) time.
- Hash Map: Provides fast O(1) average time complexity for access operations, which is essential 
  for the cache's performance.
"""

## 7. Visual / Intuition

"""
Imagine a row of buckets representing a cache. Each bucket can hold one item, and the row has 
a fixed length. When a new item comes in and the row is full, the bucket at the end is emptied 
and the new item is placed in the first bucket. If an item is reused, it moves to the front, 
shifting the other items back.
"""

## 8. Programming Patterns

"""
- Cache Eviction Pattern: Automatically removes old or less-used items to make room for new entries.
- Time-based prioritization: Uses access time to prioritize which items remain in the cache.
"""

## 9. Typical Problems

"""
- Cache Miss: When a requested item is not found in the cache, leading to a longer retrieval 
  time as the original source must be accessed.
- Cache Thrashing: Frequent evictions and insertions due to a poorly sized cache or rapidly 
  changing access patterns.
"""

## 10. Gotchas / Pitfalls

"""
- Capacity Misconfiguration: Setting the cache capacity too low might result in frequent evictions, 
  undermining the cache's purpose.
- Thread Safety: Ensuring thread-safe operations in multi-threaded environments to prevent 
  inconsistent cache state.
"""

## 11. Code Implementation (Demo of Core Operations)

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """Add new node right after head."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """Remove an existing node from the linked list."""
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """Move certain node in between to the head."""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """Pop the current tail."""
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        # Move the accessed node to the head
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        
        if not node:
            newNode = Node(key, value)
            self.cache[key] = newNode
            self._add_node(newNode)

            if len(self.cache) > self.capacity:
                # Pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
        else:
            # Update the value.
            node.value = value
            self._move_to_head(node)
```
```