# Adjacency Matrix Data Structure

```python
```python
# Adjacency Matrix Data Structure

## 1. Concept Overview

"""
An adjacency matrix is a 2D array used to represent a graph. Each cell in the matrix
indicates whether a pair of vertices is adjacent or not in the graph. For an undirected
graph with 'n' vertices, the adjacency matrix will be an 'n x n' matrix. In a directed
graph, the direction of edges is represented by the position of non-zero entries in the
matrix. Typically, a value of 1 (or a non-zero value) at matrix[i][j] indicates an edge
from vertex 'i' to vertex 'j', while a 0 indicates no edge.
"""

## 2. Implementation Details

"""
The adjacency matrix is implemented using a 2D list in Python. The matrix is initialized
with zeros, and edges are added by setting the appropriate cell to 1 (or the weight for
weighted graphs). It requires O(V^2) space where V is the number of vertices, making it
suitable for dense graphs.
"""

## 3. Core Operations & Time Complexities

"""
- Add Edge: O(1)
  To add an edge from vertex 'u' to vertex 'v', set matrix[u][v] to 1 (or weight w for 
  weighted graphs).

- Remove Edge: O(1)
  To remove an edge, set matrix[u][v] back to 0.

- Check Edge Existence: O(1)
  Check if matrix[u][v] is non-zero to confirm the presence of an edge.

- Iterate Over Neighbors: O(V)
  To find all neighbors of a vertex, you need to traverse the row corresponding to that 
  vertex, which takes O(V) time.
"""

## 4. Common Use Cases

"""
- Suitable for dense graphs where the number of edges is close to the number of vertices 
  squared.
- Used in algorithms where quick edge look-up is crucial, such as in Floyd-Warshall for 
  finding shortest paths.
- Useful in representing graphs in mathematical computations or simulations where matrix 
  operations are advantageous.
"""

## 5. Trade-offs

"""
- Pros:
  - Constant time complexity for adding, removing, and checking the existence of an edge.
  - Simple and easy to implement.
  
- Cons:
  - Inefficient use of space for sparse graphs due to O(V^2) space complexity.
  - Iterating over all edges takes O(V^2) time, which can be costly for large graphs with 
    fewer edges.
"""

## 6. Design Decisions

"""
- Choice of using a 2D list structure allows for straightforward indexing and manipulation.
- Adjacency matrices are designed with ease of edge existence checking in mind, making them 
  optimal for scenarios where this operation is frequent.
"""

## 7. Visual / Intuition

"""
Imagine a table with rows and columns corresponding to vertices of the graph. Each cell in 
this table tells you whether a direct connection (edge) exists between the pair of vertices 
represented by the row and column.
"""

## 8. Programming Patterns

"""
- Use nested loops for iterating through the matrix for actions like traversing all edges.
- List comprehensions can be used for efficiently extracting neighbors of a vertex.
"""

## 9. Typical Problems

"""
- Graph traversal problems like Depth-First Search (DFS) and Breadth-First Search (BFS).
- Shortest path algorithms such as the Floyd-Warshall algorithm.
- Graph connectivity and cycle detection problems.
"""

## 10. Gotchas / Pitfalls

"""
- Adjacency matrices are not space-efficient for graphs with a large number of vertices but 
  relatively few edges (sparse graphs).
- Modifying the matrix directly can lead to incorrect graph representations if indices are 
  mishandled.
"""

## 11. Code Implementation (Demo of Core Operations)

class Graph:
    def __init__(self, num_vertices):
        """Initializes a graph with the given number of vertices."""
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v, weight=1):
        """Adds an edge from vertex u to vertex v with the given weight (default is 1)."""
        self.adj_matrix[u][v] = weight

    def remove_edge(self, u, v):
        """Removes the edge from vertex u to vertex v."""
        self.adj_matrix[u][v] = 0

    def has_edge(self, u, v):
        """Checks if there is an edge from vertex u to vertex v."""
        return self.adj_matrix[u][v] != 0

    def get_neighbors(self, u):
        """Returns a list of neighbors for a given vertex u."""
        return [v for v in range(self.num_vertices) if self.adj_matrix[u][v] != 0]

# Example usage:
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(1, 2, 3)
print(graph.has_edge(0, 1))  # True
print(graph.get_neighbors(1))  # [2]
graph.remove_edge(0, 1)
print(graph.has_edge(0, 1))  # False
```
```