# Adjacency List Data Structure

```python
```python
# Adjacency List Data Structure

## 1. Concept Overview

"""
An adjacency list is a collection of lists or arrays used to represent a graph. 
Each vertex of the graph has a list associated with it, containing all the vertices 
adjacent to that vertex. This data structure is efficient in terms of space and is 
particularly well-suited for representing sparse graphs, where the number of edges 
is much lower than the maximal number of edges.

The adjacency list is a practical choice for many graph algorithms because it allows 
for efficient traversal of the graph's edges, enabling operations like depth-first 
search (DFS) and breadth-first search (BFS) to be performed effectively.
"""

## 2. Implementation Details

"""
An adjacency list can be implemented using a dictionary in Python, where each key 
represents a vertex, and the corresponding value is a list of vertices that are 
adjacent to it. This list can be implemented using Python's built-in list or set 
types, depending on whether the graph is directed or undirected, and whether it 
allows multiple edges between the same pair of vertices.

For a directed graph, an edge from vertex A to vertex B is represented by adding B 
to the adjacency list of A. For an undirected graph, B is also added to the adjacency 
list of A, and A is added to the adjacency list of B.
"""

## 3. Core Operations & Time Complexities

"""
- Add Vertex: O(1)
  Adding a new vertex involves inserting a new key into the dictionary with an empty list as its value.

- Add Edge: O(1)
  Adding an edge involves appending a vertex to the list of an existing vertex's adjacency list.

- Remove Vertex: O(V + E)
  Removing a vertex requires not only deleting the key from the dictionary but also removing the vertex
  from all other lists, which may involve examining all vertices and edges in the worst case.

- Remove Edge: O(E)
  Removing an edge requires locating and removing the destination vertex from the source vertex's list,
  which can take linear time in the number of edges in the worst-case scenario.

- Check for Edge: O(V)
  Checking for the existence of an edge involves searching through the list of one vertex, which can 
  take linear time in the number of edges of that vertex.
"""

## 4. Common Use Cases

"""
- Network Routing: Used to represent the network of routers and connections where the vertices are routers 
  and edges are the connections between them.

- Social Networks: Representing user profiles and friendships or connections.

- Road Maps: Cities or intersections as vertices and roads as edges.

- Web Graphs: Websites as vertices and hyperlinks as edges.
"""

## 5. Trade-offs

"""
- Space Efficiency: More space-efficient than an adjacency matrix for sparse graphs.
- Ease of Modification: Adding or removing vertices and edges can be performed efficiently.
- Edge Lookup: Less efficient than adjacency matrix for querying specific edges.
"""

## 6. Design Decisions

"""
The choice to use a dictionary to represent the adjacency list allows for efficient 
vertex addition and lookup operations. Using lists for the adjacency lists makes 
edge addition straightforward and ensures that the representation remains dynamic, 
allowing for modification at runtime.
"""

## 7. Visual / Intuition

"""
Imagine a graph as a set of nodes connected by lines. The adjacency list is like a 
table where each node has a list of the other nodes it connects directly to. This 
list tells you where you can go directly from any node.
"""

## 8. Programming Patterns

"""
- Graph Traversal: Using DFS or BFS starting from any node using the adjacency list.
- Path Finding: Implementing algorithms like Dijkstra's or A* using adjacency lists.
- Cycle Detection: Utilizing DFS in a directed graph to detect cycles.
"""

## 9. Typical Problems

"""
- Finding the shortest path between two nodes.
- Detecting cycles in directed or undirected graphs.
- Identifying connected components in a graph.
- Topological sorting of a directed acyclic graph (DAG).
"""

## 10. Gotchas / Pitfalls

"""
- When implementing an adjacency list, ensure that there are no duplicate edges for 
  undirected graphs by checking before adding an edge.
- Be careful with edge cases where the graph is empty or consists of isolated vertices.
- Ensure that removing vertices updates all adjacency lists to maintain consistency.
"""

## 11. Code Implementation (Demo of Core Operations)

class Graph:
    def __init__(self):
        """
        Initializes an empty graph with no vertices and edges.
        """
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, source, destination):
        """
        Adds a directed edge from source to destination.
        """
        if source in self.adjacency_list and destination in self.adjacency_list:
            self.adjacency_list[source].append(destination)

    def remove_edge(self, source, destination):
        """
        Removes a directed edge from source to destination.
        """
        if source in self.adjacency_list:
            try:
                self.adjacency_list[source].remove(destination)
            except ValueError:
                pass

    def remove_vertex(self, vertex):
        """
        Removes a vertex and all edges associated with it.
        """
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]
            for v in self.adjacency_list:
                try:
                    self.adjacency_list[v].remove(vertex)
                except ValueError:
                    pass

    def contains_edge(self, source, destination):
        """
        Checks if an edge exists from source to destination.
        """
        return source in self.adjacency_list and destination in self.adjacency_list[source]

    def print_graph(self):
        """
        Prints the adjacency list of the graph.
        """
        for vertex in self.adjacency_list:
            print(f"{vertex}: {self.adjacency_list[vertex]}")

# Example usage
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'C')
graph.print_graph()
```
```