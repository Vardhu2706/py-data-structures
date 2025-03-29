# Hash Table Data Structure

```python
```python
# Hash Table Data Structure

## 1. Concept Overview

"""
A hash table is a data structure that implements an associative array abstract data type, a structure that can map keys to values. 
A hash table uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

The primary advantage of a hash table is its efficiency in looking up data. The average time complexity for search, insert, and delete operations is O(1), 
making hash tables ideal for scenarios where quick data retrieval is necessary.
"""

## 2. Implementation Details

"""
A hash table typically involves:
1. **Hash Function**: Converts a given key into an integer hash, which determines the index in the array.
2. **Collision Handling**: Since different keys can hash to the same index, a strategy is needed to handle collisions. Common methods include:
   - **Chaining**: Each array index points to a linked list of entries.
   - **Open Addressing**: Finds the next available slot within the array (e.g., Linear probing, Quadratic probing, Double hashing).

The load factor, defined as the number of elements divided by the number of slots, affects performance. As the load factor increases, the likelihood of collisions increases, potentially degrading performance.
"""

## 3. Core Operations & Time Complexities

"""
- **Insert(key, value)**: O(1) on average. Place a key-value pair in the table.
- **Search(key)**: O(1) on average. Retrieve the value associated with a given key.
- **Delete(key)**: O(1) on average. Remove the key-value pair associated with a given key.

Note that the worst-case complexity for these operations can degrade to O(n) in scenarios with poor hash functions or high load factors.
"""

## 4. Common Use Cases

"""
- **Data Caching**: Fast retrieval of cached data using keys.
- **Database Indexing**: Quick access to records in a database.
- **Symbol Tables**: Compilers use hash tables to manage scopes and bindings.
- **Counting Frequency**: Efficiently count occurrences of distinct items.
"""

## 5. Trade-offs

"""
- **Pros**:
  - Fast data retrieval, insertion, and deletion with average time complexity of O(1).
  - Flexible key types, supporting a wide range of applications.

- **Cons**:
  - Potential for hash collisions, which can degrade performance.
  - Requires a good hash function to distribute keys uniformly.
  - Memory usage can be high, especially with open addressing.
"""

## 6. Design Decisions

"""
Key design considerations for implementing a hash table include:
- Choosing a suitable hash function that minimizes collisions.
- Selecting a collision resolution technique that balances performance and memory usage.
- Deciding when and how to resize the table to maintain a low load factor, generally by doubling the size when a threshold is reached.
"""

## 7. Visual / Intuition

"""
Imagine a library with a large number of books. A hash table is akin to a well-organized catalog system that quickly tells you where any book is located based on its title. 
The hash function acts as the method of organizing the catalog, determining the section where each book title (key) will be indexed.
"""

## 8. Programming Patterns

"""
- **Memoization**: Using a hash table to store previously computed results for recursive algorithms.
- **Counting Items**: Using a hash table to keep a count of occurrences of elements, such as words in a document.
- **Set Operations**: Implementing sets using hash tables for quick membership testing.
"""

## 9. Typical Problems

"""
- Implementing a hash map from scratch.
- Designing a spell checker using a hash table for dictionary lookups.
- Building a LRU (Least Recently Used) cache using a hash table for cache entries.
"""

## 10. Gotchas / Pitfalls

"""
- **Poor Hash Functions**: Can lead to many collisions, degrading performance.
- **Load Factor Management**: Failing to resize the hash table can lead to inefficient operations.
- **Thread Safety**: Not inherently thread-safe; requires additional mechanisms for concurrent use.
"""

## 11. Code Implementation (Demo of Core Operations)

class HashTable:
    def __init__(self, size=10):
        """ Initialize the hash table with given size and empty buckets. """
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash_function(self, key):
        """ Simple hash function to calculate index for a given key. """
        return hash(key) % self.size
    
    def insert(self, key, value):
        """ Insert a key-value pair into the hash table. """
        index = self._hash_function(key)
        # Check if the key already exists and update
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # If key does not exist, append new key-value
        self.table[index].append([key, value])
    
    def search(self, key):
        """ Search for a value by key in the hash table. """
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def delete(self, key):
        """ Delete a key-value pair from the hash table. """
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

# Example usage:
hash_table = HashTable()
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
print(hash_table.search("key1"))  # Output: value1
hash_table.delete("key1")
print(hash_table.search("key1"))  # Output: None
```
```