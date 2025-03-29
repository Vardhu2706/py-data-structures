# Stack Data Structure

```python
```python
# Stack Data Structure

## 1. Concept Overview

"""
A stack is a linear data structure that follows the Last In First Out (LIFO) principle, 
meaning the last element added to the stack will be the first one to be removed. 
Imagine a stack of plates where you can only add or remove the top plate. 
Stacks are used in various applications such as function call management in 
recursion, expression evaluation, and backtracking algorithms.
"""

## 2. Implementation Details

"""
Stacks can be implemented using arrays (or lists in Python) or linked lists. 
An array-based stack utilizes a list where elements are appended or popped from 
the end, providing constant time complexity for these operations. 
A linked list-based stack uses nodes where each node points to the next node. 
The head of the linked list represents the top of the stack, allowing efficient 
push and pop operations.
"""

## 3. Core Operations & Time Complexities

"""
The core operations of a stack include:

1. push(item): Adds an item to the top of the stack. Time Complexity: O(1).
2. pop(): Removes and returns the top item of the stack. Time Complexity: O(1).
3. peek(): Returns the top item of the stack without removing it. Time Complexity: O(1).
4. is_empty(): Checks if the stack is empty. Time Complexity: O(1).
5. size(): Returns the number of elements in the stack. Time Complexity: O(1).
"""

## 4. Common Use Cases

"""
- Function Call Management: Stacks manage function calls and local variables.
- Expression Evaluation: Used in syntax parsing and evaluating expressions (e.g., converting infix to postfix).
- Undo Mechanisms: Maintaining history of states for undo operations in applications.
- Backtracking Algorithms: Used in algorithms such as maze solving, where paths are explored and backtracked.
"""

## 5. Trade-offs

"""
Advantages:
- Simple and easy to implement.
- Efficient for managing data with LIFO requirements.

Disadvantages:
- Limited access to elements; only the top element is accessible.
- Can lead to stack overflow if the stack grows beyond a certain limit, particularly in recursive applications.
"""

## 6. Design Decisions

"""
Deciding between an array-based or linked list-based implementation depends on specific requirements:
- Array-based stacks are straightforward and provide O(1) amortized time for push operations but can be inefficient if resizing is needed.
- Linked list-based stacks provide dynamic sizing, avoiding overflow issues, but incur additional memory overhead due to node pointers.
"""

## 7. Visual / Intuition

"""
Visualize a stack as a vertical container where you can only add or remove items from the top. 
This visual helps in understanding the LIFO behavior of the stack.
"""

## 8. Programming Patterns

"""
- Use stacks in Depth-First Search (DFS) implementations.
- Utilize stacks for maintaining state in iterative algorithms that mimic recursion.
"""

## 9. Typical Problems

"""
- Balancing Parentheses: Check if an expression has balanced parentheses using a stack.
- Reverse Polish Notation: Evaluate expressions written in postfix notation using a stack.
- Stock Span Problem: Calculate the stock span of stocks using a stack to track price information.
"""

## 10. Gotchas / Pitfalls

"""
- Stack Overflow: Occurs when the stack exceeds its limit, particularly in recursive depth scenarios.
- Underflow: Attempting to pop an element from an empty stack can lead to underflow errors.
"""

## 11. Code Implementation (Demo of Core Operations)

class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item of the stack."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        """Return the top item of the stack without removing it."""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.items)

# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())  # Output: 3
    print(stack.peek())  # Output: 2
    print(stack.is_empty())  # Output: False
    print(stack.size())  # Output: 2
```
```