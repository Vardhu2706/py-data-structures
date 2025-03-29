# Directed Graph Data Structure

```python
```python
# Directed Graph Data Structure

## 1. Concept Overview

"""
A Directed Graph, or digraph, is a set of nodes connected by edges, where the edges have a direction associated with them. Unlike undirected graphs, where each edge is bidirectional, in a directed graph, each edge has a direction, pointing from one vertex to another. This property makes directed graphs suitable for representing asymmetric relationships between entities, such as the flow of traffic, hierarchy of tasks, or web page links.
"""

## 2. Implementation Details

"""
Directed graphs can be implemented using various data structures, the most common being:

- Adjacency List: Each vertex maintains a list of its adjacent vertices. This is space-efficient for sparse graphs.
- Adjacency Matrix: A 2D array where the element at row i and column j is true if there's an edge from vertex i to vertex j, otherwise false. This is suitable for dense graphs.

In Python, an adjacency list can be represented using a dictionary where keys are vertices and values are lists of adjacent vertices. An adjacency matrix can be represented using a 2D list (list of lists).
"""

## 3. Core Operations & Time Complexities

"""
- Add Vertex: O(1)
  Simply add a new key to the adjacency list or adjust the size of the matrix.
  
- Add Edge: O(1) for adjacency list, O(1) for adjacency matrix
  For adjacency list, append to the list of the start vertex. For adjacency matrix, set the appropriate element to True.
  
- Remove Vertex: O(V + E) for adjacency list, O(V^2) for adjacency matrix
  In the adjacency list, remove the vertex and all edges pointing to/from it. In the matrix, remove the row and column corresponding to the vertex.
  
- Remove Edge: O(E) for adjacency list, O(1) for adjacency matrix
  For adjacency list, remove the target vertex from the list of the start vertex. For adjacency matrix, set the appropriate element to False.
  
- Check if Edge Exists: O(E) for adjacency list, O(1) for adjacency matrix
  For adjacency list, check membership in the list. For adjacency matrix, check the element value.
"""

## 4. Common Use Cases

"""
- Representing networks such as social networks, where direction indicates follower relationships.
- Modeling dependencies in scheduling problems, such as task execution order in project management.
- Describing state transitions in automata or finite state machines.
- Representing web page links in a search engine's index.
"""

## 5. Trade-offs

"""
- Adjacency List: Efficient for sparse graphs, low space complexity, but checking edge existence can take longer.
- Adjacency Matrix: Simple and fast edge checks, but can consume more space for sparse graphs.
- Depending on the application, one may choose between time efficiency (matrix) and space efficiency (list).
"""

## 6. Design Decisions

"""
The choice between adjacency list and adjacency matrix should be based on:
- Graph density: Sparse graphs benefit from adjacency lists due to lower space usage.
- Frequency of edge checks: If frequent, adjacency matrix might be preferred.
- Implementation simplicity: Adjacency matrix is straightforward but not as space-efficient for sparse graphs.
"""

## 7. Visual / Intuition

"""
Visualize a directed graph as a collection of points (nodes) with arrows (edges) showing connections. Unlike undirected graphs, these arrows have a direction, indicating the start and endpoint of a relationship.
"""

## 8. Programming Patterns

"""
- Depth-First Search (DFS) and Breadth-First Search (BFS) are common patterns used to traverse or search through a directed graph.
- Topological Sorting is a technique applied to directed acyclic graphs (DAGs) to linearly order vertices based on dependencies.
- Strongly Connected Components (SCCs) are subgraphs where any pair of vertices are mutually reachable.
"""

## 9. Typical Problems

"""
- Finding the shortest path between nodes using algorithms like Dijkstra or Bellman-Ford.
- Detecting cycles in the graph to prevent infinite loops in processes.
- Determining connectivity, such as finding SCCs or checking if all nodes are reachable from a starting node.
- Scheduling tasks using topological sorting.
"""

## 10. Gotchas / Pitfalls

"""
- Forgetting about directionality can lead to incorrect assumptions about reachability or connectivity.
- Ensuring consistent updates when adding/removing vertices or edges, especially in adjacency matrices, to avoid stale data.
- Handling isolated nodes: A node with no incoming or outgoing edges should still be represented in the graph.
"""

## 11. Code Implementation (Demo of Core Operations)

class DirectedGraph:
    def __init__(self):
        """Initialize an empty directed graph using an adjacency list."""
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, start_vertex, end_vertex):
        """Add a directed edge from start_vertex to end_vertex."""
        if start_vertex in self.adjacency_list:
            self.adjacency_list[start_vertex].append(end_vertex)
        else:
            self.adjacency_list[start_vertex] = [end_vertex]

    def remove_edge(self, start_vertex, end_vertex):
        """Remove the directed edge from start_vertex to end_vertex."""
        if start_vertex in self.adjacency_list:
            try:
                self.adjacency_list[start_vertex].remove(end_vertex)
            except ValueError:
                pass

    def remove_vertex(self, vertex):
        """Remove a vertex and all edges associated with it."""
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]
        for vertices in self.adjacency_list.values():
            try:
                vertices.remove(vertex)
            except ValueError:
                pass

    def has_edge(self, start_vertex, end_vertex):
        """Check if an edge exists from start_vertex to end_vertex."""
        return start_vertex in self.adjacency_list and end_vertex in self.adjacency_list[start_vertex]

    def __str__(self):
        """Return a string representation of the graph's adjacency list."""
        return str(self.adjacency_list)

# Example usage:
graph = DirectedGraph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_edge('A', 'B')
print("Graph after adding edge A -> B:", graph)
graph.remove_edge('A', 'B')
print("Graph after removing edge A -> B:", graph)
graph.remove_vertex('A')
print("Graph after removing vertex A:", graph)
```
```