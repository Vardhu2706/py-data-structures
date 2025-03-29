# Directed Acyclic Graph (DAG) Data Structure

## 1. Concept Overview

"""
A Directed Acyclic Graph (DAG) is a graph data structure that consists of vertices and directed edges, 
with the constraint that there are no cycles. This means that it is impossible to start at any vertex v 
and follow a consistently directed path that eventually loops back to v again. DAGs are used in various 
applications, including representing structures with dependencies, scheduling, and data processing networks.
"""

## 2. Implementation Details

"""
DAGs are typically implemented using adjacency lists or adjacency matrices. An adjacency list for a DAG 
comprises a list where each index represents a vertex, and each element at that index is a list of 
vertices that are directly accessible from the vertex.

The adjacency matrix representation uses a 2D array where the cell at row i and column j is true (or holds 
a weight/value) if there is a directed edge from vertex i to vertex j. For sparse graphs, adjacency lists 
are more space-efficient, while adjacency matrices are beneficial for dense graphs or when quick edge 
existence checks are required.
"""

## 3. Core Operations & Time Complexities

"""
- Add Vertex: O(1)
  Adding a vertex is straightforward but depends on the representation. For an adjacency list, it involves 
  appending a new list; for an adjacency matrix, it involves expanding the matrix.

- Add Edge: O(1) average for adjacency list, O(1) for adjacency matrix
  Adding an edge involves updating the list for the source vertex or setting a matrix cell to true.

- Remove Vertex: O(V + E) average
  Removing a vertex involves removing all edges associated with it. This operation requires traversing all 
  vertices and adjusting their adjacency lists or matrix rows/columns.

- Remove Edge: O(E) for adjacency list, O(1) for adjacency matrix
  Removing an edge involves finding and removing the target vertex from the source vertex's adjacency list.

- Topological Sort: O(V + E)
  This operation provides a linear ordering of vertices such that for every directed edge uv, vertex u comes 
  before v. It is typically implemented using Depth-First Search (DFS) or Kahn's algorithm.
"""

## 4. Common Use Cases

"""
- Task Scheduling: DAGs are used to model tasks with dependencies for scheduling problems.
- Data Processing Pipelines: In ETL processes, DAGs are used to represent data flows and processing steps.
- Version Control: DAGs can represent changes in file versions or commits in version control systems.
- Dependency Resolution: Package management systems use DAGs to resolve dependencies between packages.
"""

## 5. Trade-offs

"""
- Space Complexity: Adjacency matrices require O(V^2) space, which can be inefficient for sparse graphs. 
  Adjacency lists have a space complexity of O(V + E), which is more efficient for sparse graphs.
- Ease of Edge Checks: Adjacency matrices allow for O(1) edge existence checks, whereas adjacency lists 
  require O(E) edge checks.
- Complexity of Operations: Adding and removing vertices and edges may have varying complexities depending 
  on the chosen representation.
"""

## 6. Design Decisions

"""
Choosing between adjacency list and adjacency matrix is a critical design decision based on expected graph 
density and operations. Adjacency lists are preferred for sparse graphs with frequent insertions and deletions, 
while adjacency matrices are ideal for dense graphs where quick edge checks are essential.
"""

## 7. Visual / Intuition

"""
Visualizing a DAG involves drawing nodes (vertices) and directed arrows (edges) between them with no 
backtracking loops. This representation emphasizes the hierarchical or directional nature of the data.
"""

## 8. Programming Patterns

"""
- Depth-First Search (DFS): Used for topological sorting and detecting cycles.
- Breadth-First Search (BFS): Useful for level-order traversal and shortest path in unweighted graphs.
- Kahn's Algorithm: A popular method for topological sorting using in-degree tracking.
"""

## 9. Typical Problems

"""
- Finding the shortest/longest path in a DAG.
- Topological sorting of vertices.
- Detecting cycles (to ensure the graph remains acyclic).
- Calculating transitive closures.
"""

## 10. Gotchas / Pitfalls

"""
- Ensuring that no cycles are introduced when adding edges is crucial to maintaining the properties of a DAG.
- Be cautious of the graph's representation choice, as it impacts performance and complexity.
- Incorrect topological sorting methods can lead to inaccurate results or runtime errors.
"""

## 11. Code Implementation (Demo of Core Operations)

class DAG:
    def __init__(self):
        """Initialize a Directed Acyclic Graph using an adjacency list."""
        self.graph = {}

    def add_vertex(self, vertex):
        """Add a vertex to the DAG."""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, start_vertex, end_vertex):
        """Add a directed edge from start_vertex to end_vertex."""
        if start_vertex not in self.graph:
            self.add_vertex(start_vertex)
        if end_vertex not in self.graph:
            self.add_vertex(end_vertex)
        self.graph[start_vertex].append(end_vertex)

    def remove_vertex(self, vertex):
        """Remove a vertex and its edges from the DAG."""
        if vertex in self.graph:
            del self.graph[vertex]
        for v in self.graph:
            if vertex in self.graph[v]:
                self.graph[v].remove(vertex)

    def remove_edge(self, start_vertex, end_vertex):
        """Remove a directed edge from start_vertex to end_vertex."""
        if start_vertex in self.graph and end_vertex in self.graph[start_vertex]:
            self.graph[start_vertex].remove(end_vertex)

    def topological_sort(self):
        """Return a topological ordering of the vertices in the DAG."""
        visited = set()
        stack = []
        
        def dfs(v):
            visited.add(v)
            for neighbour in self.graph[v]:
                if neighbour not in visited:
                    dfs(neighbour)
            stack.append(v)
        
        for vertex in self.graph:
            if vertex not in visited:
                dfs(vertex)
        
        return stack[::-1]

# Example Usage
dag = DAG()
dag.add_vertex('A')
dag.add_vertex('B')
dag.add_edge('A', 'B')
dag.add_vertex('C')
dag.add_edge('B', 'C')
print("Topological Sort:", dag.topological_sort())
