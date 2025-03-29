# Circular Buffer Data Structure

## 1. Concept Overview

"""
A Circular Buffer, also known as a ring buffer, is a fixed-size data structure that uses a single, contiguous block of memory in a circular fashion. This structure is particularly useful when a buffer needs to be efficiently reused without requiring dynamic memory allocation. It is characterized by two main pointers: the head (or read) pointer and the tail (or write) pointer. These pointers wrap around the buffer when they reach the end, allowing the buffer to be continuously utilized.

The Circular Buffer is often used in scenarios where data is produced and consumed at different rates, such as in I/O operations, streaming data, and real-time data processing.
"""

## 2. Implementation Details

"""
A Circular Buffer can be implemented using an array with two indices: head and tail. The head index indicates the position to read from, while the tail index indicates the position to write to. The buffer is considered full if incrementing the tail would make it equal to the head. The buffer is empty if the head equals the tail.

To manage the circular nature, both indices are wrapped around using the modulus operation based on the buffer's fixed size.
"""

## 3. Core Operations & Time Complexities

"""
1. `enqueue(element)`: Inserts an element at the tail of the buffer.
   - Time Complexity: O(1)

2. `dequeue()`: Removes and returns the element at the head of the buffer.
   - Time Complexity: O(1)

3. `is_full()`: Checks if the buffer is full.
   - Time Complexity: O(1)

4. `is_empty()`: Checks if the buffer is empty.
   - Time Complexity: O(1)
"""

## 4. Common Use Cases

"""
- Networking: Used in routers and network interfaces to buffer incoming/outgoing packets.
- Audio/Video Streaming: Managing streams where data is consumed and produced at varying rates.
- Producer-Consumer Problems: Situations where one thread is producing data and another is consuming.
- Real-Time Processing: Systems where input/output operations need to be handled efficiently.
"""

## 5. Trade-offs

"""
Pros:
- Fixed size ensures predictable memory usage.
- Efficient O(1) time complexity for insertions and deletions.
- No need for memory allocation/deallocation during operations.

Cons:
- Fixed size can lead to buffer overflow if not managed properly.
- Cannot dynamically resize without reallocation and copying data.
"""

## 6. Design Decisions

"""
- Opting for an array-based implementation for constant time access and predictable memory layout.
- Utilizing modulo operation to wrap the indices, ensuring efficient use of buffer space.
- Deciding on full/empty conditions: A common approach is to reserve one slot to differentiate between full and empty states.
"""

## 7. Visual / Intuition

"""
Imagine a circular track where runners (data elements) start at different points. The head runner (head index) is constantly being replaced by new runners (new data), while the tail runner (tail index) keeps catching up to the head. Once the tail reaches the head, the track is full, and any new runner must wait until the head moves forward (data is consumed).
"""

## 8. Programming Patterns

"""
- Two-pointer technique: Using head and tail pointers to manage read and write operations.
- Modulus operation: Ensuring circularity of the buffer using mathematical wrapping.
- Sentinel values: Sometimes used to mark positions in the buffer if needed.
"""

## 9. Typical Problems

"""
- Buffer Overflow: Occurs if the buffer is written beyond its capacity without sufficient reads.
- Buffer Underflow: Occurs if read operations are attempted on an empty buffer.
- Differentiating full vs empty: Requires careful management of head and tail pointers.
"""

## 10. Gotchas / Pitfalls

"""
- Mismanagement of head and tail indices can easily lead to off-by-one errors.
- Incorrectly determining the full/empty state can cause data loss or application errors.
- Over-reliance on buffer size can lead to inefficiencies if the buffer is frequently full or nearly empty.
"""

## 11. Code Implementation (Demo of Core Operations)

class CircularBuffer:
    def __init__(self, size):
        """Initialize a circular buffer with a fixed size."""
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.full = False

    def enqueue(self, item):
        """Insert an element into the buffer."""
        if self.full:
            raise OverflowError("Circular Buffer is full")
        
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size
        if self.tail == self.head:
            self.full = True

    def dequeue(self):
        """Remove and return the oldest element from the buffer."""
        if self.is_empty():
            raise IndexError("Circular Buffer is empty")

        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.size
        self.full = False
        return item

    def is_full(self):
        """Check if the buffer is full."""
        return self.full

    def is_empty(self):
        """Check if the buffer is empty."""
        return not self.full and self.head == self.tail

# Example usage:
# buffer = CircularBuffer(5)
# buffer.enqueue(1)
# buffer.enqueue(2)
# print(buffer.dequeue())  # Output: 1
# print(buffer.is_empty()) # Output: False
