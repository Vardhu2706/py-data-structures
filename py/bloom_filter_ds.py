# Bloom Filter Data Structure

## 1. Concept Overview

"""
A Bloom Filter is a probabilistic data structure used to test whether an element is a member of a set. It is designed for space efficiency and allows for fast insertions and membership tests. However, it may produce false positives, meaning it might incorrectly report that an element is present when it is not. False negatives, on the other hand, are not possible; if a Bloom Filter indicates an element is not present, it is definitely not in the set.

The Bloom Filter uses multiple hash functions to map elements to a fixed-size bit array. For each element inserted, the bits at the positions determined by the hash functions are set to 1. To test for membership, the bit array is checked at the positions specified by the hash functions. If all bits are set to 1, the element is considered potentially in the set; if any bit is 0, the element is definitely not in the set.
"""

## 2. Implementation Details

"""
A Bloom Filter requires:
- A bit array of m bits, all initially set to 0.
- k different hash functions, each of which maps an element to one of the m array positions with a uniform random distribution.

The choice of k and m is crucial as it affects the probability of false positives. Typically, the optimal number of hash functions k is (m/n) * ln(2), where n is the number of expected elements to be inserted.

In terms of implementation, hash functions can be constructed using cryptographic hash functions like SHA-256, combined with a modulus operation to ensure the output is within the range of the bit array size.
"""

## 3. Core Operations & Time Complexities

"""
The core operations of a Bloom Filter include:

1. Insert
   - Time Complexity: O(k)
   - Procedure: Apply the k hash functions to the element to find k positions in the bit array, and set each position to 1.
   
2. Check Membership
   - Time Complexity: O(k)
   - Procedure: Apply the k hash functions to the element to find k positions in the bit array. If any of these positions is 0, the element is definitely not in the set. If all are 1, the element may be in the set (with some probability of false positive).

The time complexity is O(k) for both operations because each involves computing k hash functions.
"""

## 4. Common Use Cases

"""
Bloom Filters are commonly used in:
- Databases, to filter out non-existent keys before accessing the database, reducing disk reads.
- Distributed systems, to efficiently check membership of an element in a large distributed dataset.
- Caching, to prevent caching of duplicates.
- Network algorithms, such as packet routing and email filtering.
"""

## 5. Trade-offs

"""
- Space Efficiency vs. False Positives: Bloom Filters use minimal space compared to other data structures like sets but at the cost of false positives.
- Lack of Deletion: Standard Bloom Filters do not support removing elements without increasing the false positive rate.
- Fixed Size: The size of the Bloom Filter is fixed at initialization and cannot be changed without reconstructing it.
"""

## 6. Design Decisions

"""
Design considerations for a Bloom Filter include:
- Choosing the optimal size of the bit array (m) and the number of hash functions (k) based on the expected number of elements (n) and acceptable false positive rate (p).
- Selecting robust hash functions to minimize collisions and ensure a uniform distribution of hash values across the bit array.
"""

## 7. Visual / Intuition

"""
Visualizing a Bloom Filter can be done by imagining a long row of bits, each initially set to 0. As elements are inserted, specific bits are set to 1 based on hash functions. Checking membership involves verifying if all the relevant bits for an element are set to 1. If any bit is 0, the element is not present.
"""

## 8. Programming Patterns

"""
Programming patterns for Bloom Filters often involve:
- Combining multiple hash functions using a single robust hash function and varying seeds or salts.
- Using bit manipulation techniques for efficient storage and access.
- Employing probabilistic techniques to balance false positive rates and space complexity.
"""

## 9. Typical Problems

"""
Typical problems involving Bloom Filters include:
- Tuning the parameters (m, k) to achieve a desired false positive rate.
- Handling the lack of a delete operation in scenarios where items need to be removed.
- Integrating with other data structures to provide a composite solution for large-scale data processing.
"""

## 10. Gotchas / Pitfalls

"""
- Overloading the Bloom Filter beyond its intended capacity increases false positive rates significantly.
- Choosing suboptimal hash functions can lead to poor distribution of bits and increased collisions.
- Not accounting for the probabilistic nature, leading to misuse in applications requiring certainty.
"""

## 11. Code Implementation (Demo of Core Operations)

"""
Below is a Python implementation of a simple Bloom Filter with basic insert and membership check operations.
"""

import hashlib

class BloomFilter:
    def __init__(self, size, hash_count):
        """Initialize the Bloom Filter with the size of the bit array and the number of hash functions."""
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        """Generate k hash values for the given item."""
        result = []
        for i in range(self.hash_count):
            hash_result = hashlib.sha256((item + str(i)).encode('utf-8')).hexdigest()
            result.append(int(hash_result, 16) % self.size)
        return result

    def add(self, item):
        """Insert an item into the Bloom Filter."""
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = 1

    def check(self, item):
        """Check whether an item is in the Bloom Filter."""
        for hash_value in self._hashes(item):
            if self.bit_array[hash_value] == 0:
                return False
        return True

# Example usage
bloom = BloomFilter(size=1000, hash_count=5)
bloom.add("hello")
bloom.add("world")

print(bloom.check("hello"))  # Output: True
print(bloom.check("world"))  # Output: True
print(bloom.check("python"))  # Output: False (most likely, but not guaranteed)
