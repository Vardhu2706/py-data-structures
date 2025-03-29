# Hash Set Data Structure

```python
```python
# Hash Set Data Structure

## 1. Concept Overview

"""
A Hash Set is a data structure that implements a set abstraction using a hash table. 
It is designed to store unique elements and allows for efficient membership testing, 
insertions, and deletions. The primary operations of a hash set include adding an 
element, removing an element, and checking if an element exists within the set. 
These operations are typically expected to run in constant time, O(1), on average.
"""

## 2. Implementation Details

"""
The Hash Set is implemented using a hash table where each element is hashed to 
determine its index in an underlying array, often referred to as a bucket. 
To handle collisions, where two different elements hash to the same index, 
a common strategy is to use chaining, where each bucket points to a list of elements.

1. **Hash Function**: A good hash function distributes elements uniformly across buckets,
   minimizing collisions and ensuring efficient operations.

2. **Collision Resolution**: Chaining is used to store elements in a linked list 
   or another collection within each bucket.

3. **Load Factor**: This is the ratio of the number of elements to the number of buckets. 
   To maintain efficiency, the hash table is resized when the load factor exceeds a 
   certain threshold (e.g., 0.75), redistributing elements across a larger number of buckets.
"""

## 3. Core Operations & Time Complexities

"""
1. **Add(element)**: Adds an element to the set if it is not already present.
   - Average Time Complexity: O(1)
   - Worst-case Time Complexity: O(n) (when all elements hash to the same bucket)

2. **Remove(element)**: Removes an element from the set if it exists.
   - Average Time Complexity: O(1)
   - Worst-case Time Complexity: O(n)

3. **Contains(element)**: Checks if an element is present in the set.
   - Average Time Complexity: O(1)
   - Worst-case Time Complexity: O(n)
"""

## 4. Common Use Cases

"""
- **Membership Testing**: Quickly determine if an element is part of a collection.
- **Unique Collection**: Maintain a collection of unique items without duplicates.
- **Set Operations**: Efficiently perform union, intersection, and difference operations.
"""

## 5. Trade-offs

"""
- **Pros**:
  - Average constant time complexity for core operations.
  - Simple implementation with chaining for collision resolution.
  
- **Cons**:
  - Memory overhead due to underlying array and potential chains.
  - Performance degrades if hash function is poor or load factor is too high.
"""

## 6. Design Decisions

"""
- **Hash Function**: Choice of a good hash function is critical to ensure even distribution.
- **Collision Resolution Strategy**: Chaining is chosen for simplicity and flexibility.
- **Resizing Strategy**: Resizing the hash table helps maintain performance as more elements are added.
"""

## 7. Visual / Intuition

"""
Imagine a row of boxes (buckets) where each box can hold multiple items (chaining). 
When you add an item, you decide which box to place it in based on a calculated position 
(hash function). If another item is placed in the same box, it is simply added to the list of items.
"""

## 8. Programming Patterns

"""
- **Set Operations**: Use hash sets to implement set operations like union, intersection, 
  and difference efficiently.
- **Deduplication**: Utilize hash sets to remove duplicates from a list.
"""

## 9. Typical Problems

"""
- **Unique Elements**: Determine the number of unique elements in a list.
- **Intersection of Arrays**: Find common elements between two arrays.
- **Duplicate Detection**: Identify if a list contains duplicates.
"""

## 10. Gotchas / Pitfalls

"""
- **Poor Hash Function**: Can lead to excessive collisions and degrade performance.
- **Load Factor Mismanagement**: Not resizing the hash table appropriately can lead to inefficiencies.
- **Mutable Elements**: Using mutable types as elements can lead to unintended behavior if they are modified after insertion.
"""

## 11. Code Implementation (Demo of Core Operations)

class HashSet:
    def __init__(self, initial_capacity=10, load_factor_threshold=0.75):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]
        self.load_factor_threshold = load_factor_threshold

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_buckets:
            for key in bucket:
                self.add(key)

    def add(self, key):
        if self.contains(key):
            return  # Element already exists
        if self.size / self.capacity > self.load_factor_threshold:
            self._resize()

        bucket_index = self._hash(key)
        self.buckets[bucket_index].append(key)
        self.size += 1

    def remove(self, key):
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        
        for i, element in enumerate(bucket):
            if element == key:
                del bucket[i]
                self.size -= 1
                return

    def contains(self, key):
        bucket_index = self._hash(key)
        return key in self.buckets[bucket_index]

# Example usage:
hash_set = HashSet()
hash_set.add("apple")
hash_set.add("banana")
print(hash_set.contains("apple"))   # True
print(hash_set.contains("cherry"))  # False
hash_set.remove("apple")
print(hash_set.contains("apple"))   # False
```
```