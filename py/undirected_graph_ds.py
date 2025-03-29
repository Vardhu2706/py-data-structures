# Undirected Graph Data Structure

## 1. Concept Overview

"""
An undirected graph is a data structure consisting of a set of vertices (nodes) and a set of edges (connections) that connect pairs of vertices. Unlike directed graphs, the edges in an undirected graph do not have a direction; they are bidirectional. This means that if there is an edge between vertex A and vertex B, it can be traversed from A to B and from B to A. 

Undirected graphs are commonly used to model relationships where the connections are mutual or bidirectional, such as in social networks, transportation networks, and biological networks.
"""

## 2. Implementation Details

"""
Undirected graphs can be implemented using various data structures:

1. **Adjacency List**: This is the most common implementation. Each vertex maintains a list of adjacent vertices. This representation is space-efficient for sparse graphs.

2. **Adjacency Matrix**: This is a 2D array where each cell (i, j) is true if there is an edge between vertex i and vertex j. This representation is less space-efficient but allows quicker edge lookup.

3. **Edge List**: A list of all edges represented as pairs of vertices. This is useful for algorithms that need to process edges directly.

In this documentation, we will focus on the adjacency list representation.
"""

## 3. Core Operations & Time Complexities

"""
1. **Add Vertex**: Add a new vertex to the graph.
   - Time Complexity: O(1)

2. **Add Edge**: Add a new edge between two vertices.
   - Time Complexity: O(1)

3. **Remove Vertex**: Remove a vertex and all associated edges.
   - Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.

4. **Remove Edge**: Remove an edge between two vertices.
   - Time Complexity: O(V) in the worst case due to the need to search the adjacency list.

5. **Search/Check for Edge**: Check if there is an edge between two vertices.
   - Time Complexity: O(V) in the worst case.

6. **Traverse**: Visit all the vertices in the graph (typically via BFS or DFS).
   - Time Complexity: O(V + E)
"""

## 4. Common Use Cases

"""
1. **Social Networks**: Modeling connections between people.
2. **Transportation Networks**: Roads and intersections.
3. **Biological Networks**: Protein interactions.
4. **Collaboration Graphs**: Co-authorship in research.
"""

## 5. Trade-offs

"""
- **Space vs. Time**: Adjacency lists are space-efficient for sparse graphs, while adjacency matrices provide faster edge checks for dense graphs.
- **Ease of Use**: Adjacency lists are generally easier to implement and use for most applications.
- **Performance**: Operations like edge lookups can be slower in adjacency lists compared to matrices.
"""

## 6. Design Decisions

"""
The choice of representation (adjacency list, matrix, or edge list) should be based on the graph's density and the operations that need to be optimized. Sparse graphs typically favor adjacency lists, while dense graphs may benefit from adjacency matrices.
"""

## 7. Visual / Intuition

"""
Visualize an undirected graph as a collection of points connected by lines. Each line represents a relationship that can be traversed in both directions, symbolizing a mutual or bi-directional relationship.
"""

## 8. Programming Patterns

"""
- **Graph Traversal**: Use Depth-First Search (DFS) or Breadth-First Search (BFS) for exploring the graph.
- **Graph Search**: Algorithms like Dijkstra's or Kruskal's for shortest paths and minimum spanning tree problems.
"""

## 9. Typical Problems

"""
1. **Connected Components**: Finding all subsets of connected nodes.
2. **Cycle Detection**: Checking if the graph contains any cycles.
3. **Graph Coloring**: Assigning colors to vertices so that no two adjacent vertices share the same color.
4. **Shortest Path**: Finding the shortest path between two vertices.
"""

## 10. Gotchas / Pitfalls

"""
- **Self-loops**: Ensure that self-loops are handled correctly if they are allowed.
- **Parallel Edges**: Be cautious of multiple edges between the same vertices if not allowed in your application.
- **Disconnected Graphs**: Handle scenarios where the graph may be disconnected.
"""

## 11. Code Implementation (Demo of Core Operations)

class UndirectedGraph:
    def __init__(self):
        """Initialize an empty graph with an adjacency list."""
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Add an edge between two vertices."""
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def remove_vertex(self, vertex):
        """Remove a vertex and all edges connected to it."""
        if vertex in self.adjacency_list:
            # Remove all edges to this vertex
            for neighbor in self.adjacency_list[vertex]:
                self.adjacency_list[neighbor].remove(vertex)
            # Remove the vertex from the graph
            del self.adjacency_list[vertex]

    def remove_edge(self, vertex1, vertex2):
        """Remove an edge between two vertices."""
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].remove(vertex2)
            if vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].remove(vertex1)

    def has_edge(self, vertex1, vertex2):
        """Check if there is an edge between two vertices."""
        return vertex2 in self.adjacency_list.get(vertex1, [])

    def __str__(self):
        """Return a string representation of the graph."""
        return str(self.adjacency_list)

# Example usage:
graph = UndirectedGraph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_edge('A', 'B')
print(graph)  # Output: {'A': ['B'], 'B': ['A']}
