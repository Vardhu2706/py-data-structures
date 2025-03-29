# Rolling Hash Data Structure

```python
```python
# Rolling Hash Data Structure

## 1. Concept Overview

"""
The Rolling Hash is a hash function designed to compute a hash value for a sliding window of data efficiently.
This is particularly useful in string algorithms, where it can be used to find patterns or substrings in a larger text.
The fundamental concept involves computing the hash of a substring based on the hash of the previous substring,
allowing for rapid updates as the window slides through the data.

The technique leverages modular arithmetic to manage hash values, maintaining a constant-time complexity for each update.
Unlike traditional hashing methods that require recalculating the entire hash upon each window shift,
the Rolling Hash updates incrementally, subtracting the old character and adding the new character.
"""

## 2. Implementation Details

"""
A typical implementation involves choosing a base (b) and a large prime modulus (m).
The choice of base and modulus affects the hash's collision resistance and efficiency.
The hash for a substring can be calculated using the formula:

    hash(s) = (s[0]*b^(n-1) + s[1]*b^(n-2) + ... + s[n-1]*b^0) % m

Where `n` is the length of the substring. As the window slides, the hash is updated by removing the contribution of
the outgoing character and adding the contribution of the incoming character.
"""

## 3. Core Operations & Time Complexities

"""
- Initialization: O(n), where n is the length of the initial substring.
- Hash Update (Slide Window): O(1), involves a constant number of arithmetic operations.
- Full Recalculation (optional): O(n), recalculating hash from scratch for validation.
"""

## 4. Common Use Cases

"""
- Substring search algorithms, such as Rabin-Karp.
- Detecting duplicates in a subset of data.
- Plagiarism detection by comparing document fragments.
- Network data synchronization where small changes need quick detection.
"""

## 5. Trade-offs

"""
- Collision Risk: Choosing a small modulus increases the likelihood of hash collisions.
- Numerical Stability: Large integers due to high base values can cause overflow, although Python handles large integers gracefully.
- Modulus Dependency: Performance is sensitive to the choice of base and modulus.
"""

## 6. Design Decisions

"""
- Base and Modulus Choice: Typically, base is a small prime number, and modulus is a large prime.
- Window Size: Determines the update efficiency and hash significance.
- Hash Function: Needs to be fast and collision-resistant.
"""

## 7. Visual / Intuition

"""
Imagine a sliding window of fixed size moving across a string. As the window moves one character forward, 
the hash value updates by removing the first character's contribution and adding the new character's contribution.
This process is akin to a conveyor belt, where the hash value is the sum of weighted character positions.
"""

## 8. Programming Patterns

"""
- Sliding Window Technique: Efficiently moving through data and updating state.
- Modular Arithmetic: Used for managing overflow and ensuring consistent hash values.
- Incremental Updates: Essential for maintaining efficient time complexity.
"""

## 9. Typical Problems

"""
- Substring Search: Detecting substring presence efficiently in a larger string.
- Duplicate Detection: Identifying repeated patterns within a dataset.
- Hash Collisions: Managing and detecting hash collisions through careful base/modulus choice.
"""

## 10. Gotchas / Pitfalls

"""
- Overflow: Although Python handles large integers, other languages might not, requiring careful handling of large values.
- Collision Handling: Be mindful of potential hash collisions when base/modulus values are not well chosen.
- Modulus Choice: Small modulus increases collision risk, while too large can affect performance.
"""

## 11. Code Implementation (Demo of Core Operations)

def compute_initial_hash(s, base, modulus):
    """Compute the hash for the initial window."""
    hash_value = 0
    n = len(s)
    for i in range(n):
        hash_value = (hash_value * base + ord(s[i])) % modulus
    return hash_value

def roll_hash(old_hash, old_char, new_char, power, base, modulus):
    """Compute the new hash when the window slides by one character."""
    new_hash = (old_hash * base + ord(new_char) - ord(old_char) * power) % modulus
    # Ensure positive hash value
    if new_hash < 0:
        new_hash += modulus
    return new_hash

# Example usage
def example_usage():
    base = 256
    modulus = 101
    text = "hello world"
    pattern_length = 5
    
    initial_window = text[:pattern_length]
    initial_hash = compute_initial_hash(initial_window, base, modulus)
    
    # Pre-compute base^(pattern_length-1) % modulus
    power = pow(base, pattern_length - 1, modulus)
    
    current_hash = initial_hash
    for i in range(len(text) - pattern_length):
        # Slide the window by one character
        current_hash = roll_hash(current_hash, text[i], text[i + pattern_length], power, base, modulus)
        print(f"Updated hash after sliding: {current_hash}")

example_usage()
```
```