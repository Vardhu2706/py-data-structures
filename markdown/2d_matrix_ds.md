# 2D Matrix Data Structure

```python
```python
# 2D Matrix Data Structure

## 1. Concept Overview

"""
A 2D Matrix is a fundamental data structure in computer science used to store data in a tabular form. It consists of rows and columns, forming a grid-like structure. Each element in the matrix can be accessed by specifying a pair of indices: one for the row and one for the column. This data structure is particularly useful for representing relational data, performing mathematical operations, and handling spatial data like images.

The matrix is often implemented as a list of lists in Python, where each inner list represents a row. This allows efficient access to elements using the row and column indices.
"""

## 2. Implementation Details

"""
The most common way to implement a 2D matrix in Python is by using nested lists. This involves creating a list where each element is another list representing a row of the matrix. The following are key points regarding this implementation:

- **Row-Major Order:** The matrix is stored in row-major order, meaning that rows are stored one after the other.
- **Dynamic Sizing:** Python lists are dynamic, so the size of the matrix (number of rows and columns) can be changed at runtime.
- **Access Time:** Accessing an element at a specific row and column index is O(1) due to direct index-based access.
- **Memory Usage:** The memory usage grows linearly with the number of elements, O(m * n) for a matrix with m rows and n columns.
"""

## 3. Core Operations & Time Complexities

"""
1. **Access an element:** O(1)
   Accessing a matrix element by its indices is a constant time operation as lists support direct access.

2. **Modify an element:** O(1)
   Modifying an element at a specific index is also a constant time operation.

3. **Add a row or column:**
   - Add a row: O(n) where n is the number of columns, since a new list (row) needs to be appended.
   - Add a column: O(m) where m is the number of rows, as each row must be traversed to append a new element.

4. **Delete a row or column:**
   - Delete a row: O(n) where n is the number of columns, due to removing a list.
   - Delete a column: O(m) where m is the number of rows, as each row must be traversed to remove an element.
"""

## 4. Common Use Cases

"""
- **Mathematical Computations:** Used in linear algebra for matrix operations like multiplication, addition, and transposition.
- **Graph Representations:** Adjacency matrices are used to represent graphs.
- **Image Processing:** Used to represent pixel grids in images.
- **Game Development:** Grids for board games like tic-tac-toe or chess.
- **Dynamic Programming:** Used in algorithms like the Floyd-Warshall for shortest paths or in solving the knapsack problem.
"""

## 5. Trade-offs

"""
- **Ease of Access vs. Memory Usage:** While a 2D matrix allows for easy access and manipulation of data, it can consume a significant amount of memory, especially for large matrices.
- **Fixed vs. Dynamic Size:** In languages with static typing, matrices may have fixed sizes, offering performance benefits, whereas Python's dynamic lists allow for more flexibility at the cost of potential performance overhead.
- **Sparse vs. Dense:** For matrices with a large number of zero or null values, a sparse matrix representation may be more memory efficient.
"""

## 6. Design Decisions

"""
- **Data Type Flexibility:** Python lists allow for different data types within the same matrix, providing flexibility but also requiring careful handling to avoid type errors.
- **Indexing Convention:** Typically, matrices are indexed starting from zero, consistent with most programming languages.
- **Error Handling:** Implementing bounds checking can prevent index errors, ensuring robust matrix operations.
"""

## 7. Visual / Intuition

"""
Consider a 3x3 matrix:
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
Visualize this as a grid with three rows and three columns. Accessing an element involves selecting a specific cell by its row and column number, e.g., element at (1, 2) is 6.
"""

## 8. Programming Patterns

"""
- **Iteration:** Iterate over rows or columns using nested loops.
- **Matrix Transpose:** Swap rows with columns.
- **Row/Column Sum:** Calculate the sum of elements in a specific row or column.
"""

## 9. Typical Problems

"""
- **Matrix Multiplication:** Given two matrices, compute their product.
- **Matrix Rotation:** Rotate a matrix by 90 degrees clockwise or counterclockwise.
- **Path Finding:** Use a matrix to find paths in grid-based maps.
"""

## 10. Gotchas / Pitfalls

"""
- **Index Errors:** Ensure indices are within bounds to avoid runtime errors.
- **Mutable Default Arguments:** Avoid using lists as default arguments in functions to prevent unintended side effects.
- **Inefficient Operations:** Beware of inefficient operations, such as repeatedly inserting or deleting elements in large matrices.
"""

## 11. Code Implementation (Demo of Core Operations)

def create_matrix(rows, cols, default_value=0):
    """Create a 2D matrix with a specified number of rows and columns."""
    return [[default_value for _ in range(cols)] for _ in range(rows)]

def access_element(matrix, row, col):
    """Access an element in the matrix at a specified row and column."""
    return matrix[row][col]

def modify_element(matrix, row, col, value):
    """Modify an element in the matrix at a specified row and column."""
    matrix[row][col] = value

def add_row(matrix, new_row):
    """Add a new row to the matrix."""
    matrix.append(new_row)

def add_column(matrix, new_col):
    """Add a new column to the matrix."""
    for i in range(len(matrix)):
        matrix[i].append(new_col[i])

def delete_row(matrix, row_index):
    """Delete a row from the matrix."""
    matrix.pop(row_index)

def delete_column(matrix, col_index):
    """Delete a column from the matrix."""
    for row in matrix:
        row.pop(col_index)

# Example Usage
matrix = create_matrix(3, 3, 1)
print("Initial Matrix:", matrix)
accessed_value = access_element(matrix, 1, 1)
print("Accessed Element at (1, 1):", accessed_value)
modify_element(matrix, 1, 1, 5)
print("Modified Matrix:", matrix)
add_row(matrix, [7, 8, 9])
print("Matrix after Adding a Row:", matrix)
add_column(matrix, [0, 0, 0, 0])
print("Matrix after Adding a Column:", matrix)
delete_row(matrix, 2)
print("Matrix after Deleting a Row:", matrix)
delete_column(matrix, 3)
print("Matrix after Deleting a Column:", matrix)
```
```