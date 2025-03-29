# Circular Queue Data Structure

```python
```python
# Circular Queue Data Structure

## 1. Concept Overview

"""
A Circular Queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle 
and the last position is connected back to the first position to make a circle. This structure is also called a "Ring Buffer". 
Circular queues are useful in situations where the queue has a fixed size, and you need to reuse the space of the elements 
that have been dequeued. This helps in efficient memory utilization.
"""

## 2. Implementation Details

"""
A Circular Queue can be implemented using an array and two pointers: 'front' to track the front of the queue, and 'rear' to track 
the end of the queue. The 'rear' pointer increments as elements are enqueued and the 'front' pointer increments as elements are 
dequeued. When either pointer reaches the end of the array, it wraps around to the beginning of the array, hence maintaining 
the circular nature of the queue. The queue is full when the next position of 'rear' is 'front', and it is empty when 'front' 
equals 'rear'.
"""

## 3. Core Operations & Time Complexities

"""
1. Enqueue: Inserts an element at the rear of the queue.
   - Time Complexity: O(1)

2. Dequeue: Removes an element from the front of the queue.
   - Time Complexity: O(1)

3. Front: Returns the front element of the queue without removing it.
   - Time Complexity: O(1)

4. Rear: Returns the rear element of the queue without removing it.
   - Time Complexity: O(1)

5. isEmpty: Checks if the queue is empty.
   - Time Complexity: O(1)

6. isFull: Checks if the queue is full.
   - Time Complexity: O(1)
"""

## 4. Common Use Cases

"""
1. CPU scheduling, where tasks are scheduled in a circular order.
2. Memory management, particularly in managing buffers in networking.
3. In scenarios where a fixed memory size is required and memory needs to be reused efficiently.
4. Real-time data stream processing, where continuous data needs to be managed in a cyclic manner.
"""

## 5. Trade-offs

"""
1. Fixed Size: Circular queues have a fixed size, limiting the number of elements they can hold.
2. Space Efficiency: They are efficient in terms of memory usage because they reuse space of dequeued elements.
3. Complexity: Circular logic can introduce complexity over using a simple linear queue.
4. Implementation Overhead: Requires careful management of pointers for correct functioning.
"""

## 6. Design Decisions

"""
1. Array-Based vs. Node-Based: Circular queues can be implemented using arrays or linked lists. Arrays provide constant-time 
   access but need a fixed size, while linked lists can dynamically grow but have additional overhead for node management.
2. Handling Full/Empty States: Implementers must carefully decide how to distinguish between full and empty states, often using 
   a count of elements or the convention that a full queue has one less usable space than the array size.
"""

## 7. Visual / Intuition

"""
Imagine a circular track with a limited number of lanes. Cars (elements) enter the track at the rear and exit at the front. 
Once a car leaves, its lane becomes available for new cars to enter. If all lanes are occupied, new cars must wait for a lane 
to become available. This circular nature ensures that available space is reused efficiently.
"""

## 8. Programming Patterns

"""
Circular queues are often used in producer-consumer problems for buffering. The producer adds data to the queue, and the 
consumer retrieves it. This pattern helps in managing workflows where producers and consumers operate at different rates.
"""

## 9. Typical Problems

"""
1. Implementing a circular buffer for real-time data streams.
2. Designing a task scheduler using circular queues.
3. Creating a bounded buffer for inter-process communication.
"""

## 10. Gotchas / Pitfalls

"""
1. Off-by-One Errors: Careful attention is needed to manage the pointers ('front' and 'rear') correctly to avoid off-by-one 
   errors, especially when wrapping around the array.
2. Overwriting Data: Without proper checks, it's possible to overwrite data in a circular queue if it's full.
3. Empty vs Full: Properly distinguishing between full and empty states can be tricky and often requires an additional variable 
   to track the number of elements.
"""

## 11. Code Implementation (Demo of Core Operations)

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def isEmpty(self):
        return self.front == -1

    def enqueue(self, data):
        if self.isFull():
            print("Queue is full")
            return
        if self.front == -1:  # First element to be inserted
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print(f"Inserted {data}")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        data = self.queue[self.front]
        if self.front == self.rear:  # Queue has only one element
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Deleted {data}")
        return data

    def frontElement(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def rearElement(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.queue[self.rear]

# Example usage:
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
print("Front element is:", cq.frontElement())
print("Rear element is:", cq.rearElement())
cq.dequeue()
cq.enqueue(60)
print("Front element is:", cq.frontElement())
print("Rear element is:", cq.rearElement())
```
```