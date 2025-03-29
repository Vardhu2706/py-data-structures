# Graph Data Structure

## 1. Concept Overview

"""
A graph is a data structure that consists of a set of nodes (or vertices) and a set of edges that connect pairs of nodes. Graphs can be directed or undirected, weighted or unweighted. In a directed graph, edges have a direction, meaning they go from one vertex to another, while in an undirected graph, edges have no direction. In a weighted graph, each edge has an associated weight or cost, which can represent distance, time, or any other measure. Graphs are used to represent various real-world structures like social networks, transportation networks, and dependency graphs.
"""

## 2. Implementation Details

"""
Graphs can be implemented using various methods, with adjacency lists and adjacency matrices being the most common.

1. Adjacency List:
   - Each vertex maintains a list of adjacent vertices.
   - Efficiently handles sparse graphs with fewer edges.
   - Memory usage is O(V + E), where V is the number of vertices and E is the number of edges.

2. Adjacency Matrix:
   - A 2D array where element at row i and column j represents the presence (and possibly weight) of an edge between vertex i and vertex j.
   - Suitable for dense graphs with many edges.
   - Memory usage is O(V^2), which can be inefficient for large graphs with few edges.
"""

## 3. Core Operations & Time Complexities

"""
1. Add Vertex:
   - Time Complexity: O(1) for adjacency list, O(V^2) for adjacency matrix if resizing is needed.

2. Add Edge:
   - Time Complexity: O(1) for adjacency list (append operation), O(1) for adjacency matrix (updating an element).

3. Remove Vertex:
   - Time Complexity: O(V + E) for adjacency list, O(V^2) for adjacency matrix.

4. Remove Edge:
   - Time Complexity: O(E) for adjacency list (search operation), O(1) for adjacency matrix.

5. Check for Edge:
   - Time Complexity: O(E) for adjacency list, O(1) for adjacency matrix.

6. Traverse Graph (Breadth-First Search or Depth-First Search):
   - Time Complexity: O(V + E) for both adjacency list and adjacency matrix.
"""

## 4. Common Use Cases

"""
1. Social Networks: Representing user connections and interactions.
2. Navigation Systems: Modeling maps and routes with weighted edges.
3. Dependency Management: Managing build systems or package dependencies.
4. Network Flow: Analyzing traffic flow or optimizing resource distribution.
"""

## 5. Trade-offs

"""
- Adjacency List vs. Adjacency Matrix:
  - Adjacency lists are more memory-efficient for sparse graphs, while adjacency matrices allow for faster edge checks in dense graphs.
- Directionality:
  - Directed graphs can model asymmetric relationships, while undirected graphs are simpler and can model symmetric relationships.
- Weight:
  - Weighted graphs can represent more complex relationships, but require additional storage and processing.
"""

## 6. Design Decisions

"""
When designing a graph data structure, consider:
- The expected density of the graph (sparse vs. dense).
- The operations that will be most frequently performed (add/remove edges vs. vertex traversal).
- Whether edge weights or directions are needed.
- Potential scalability concerns and the trade-off between time complexity and memory usage.
"""

## 7. Visual / Intuition

"""
Visualize a graph as a network of interconnected points. For an undirected graph, think of it as a map where roads (edges) connect cities (nodes). For directed graphs, imagine one-way streets where travel is only possible in specified directions. Graphs can be cyclic (containing loops) or acyclic (having no loops), which affects traversal and search algorithms.
"""

## 8. Programming Patterns

"""
1. Graph Traversal: Use BFS or DFS to explore nodes and edges.
2. Shortest Path: Implement algorithms like Dijkstra's or Bellman-Ford for weighted graphs.
3. Connectivity: Use Union-Find algorithms to determine connected components.
4. Cycle Detection: Apply DFS-based techniques or Union-Find for cycle detection in graphs.
"""

## 9. Typical Problems

"""
1. Finding the shortest path between nodes.
2. Determining if a graph is connected.
3. Detecting cycles in a graph.
4. Finding a minimum spanning tree (e.g., using Kruskal's or Prim's algorithm).
5. Solving network flow problems (e.g., using Ford-Fulkerson algorithm).
"""

## 10. Gotchas / Pitfalls

"""
- When using an adjacency matrix, be cautious of space complexity for large graphs.
- Watch out for cycles in graphs when performing traversal operations, as they can lead to infinite loops if not handled properly.
- In directed graphs, remember that the presence of an edge from node A to node B does not imply an edge from node B to node A.
- Be mindful of zero-weight edges in weighted graphs, which can affect algorithms assuming positive weights.
"""

## 11. Code Implementation (Demo of Core Operations)

class Graph:
    def __init__(self):
        """Initializes an empty graph with an adjacency list."""
        self.adj_list = {}

    def add_vertex(self, vertex):
        """Adds a vertex to the graph."""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, u, v):
        """Adds a directed edge from u to v."""
        if u in self.adj_list:
            self.adj_list[u].append(v)
        else:
            self.adj_list[u] = [v]

    def remove_vertex(self, vertex):
        """Removes a vertex and all its edges from the graph."""
        if vertex in self.adj_list:
            self.adj_list.pop(vertex)
        for vertices in self.adj_list.values():
            if vertex in vertices:
                vertices.remove(vertex)

    def remove_edge(self, u, v):
        """Removes the edge from u to v."""
        if u in self.adj_list and v in self.adj_list[u]:
            self.adj_list[u].remove(v)

    def has_edge(self, u, v):
        """Checks if there is an edge from u to v."""
        return u in self.adj_list and v in self.adj_list[u]

    def bfs(self, start):
        """Performs a breadth-first search starting from the given vertex."""
        visited = set()
        queue = [start]
        result = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend([v for v in self.adj_list.get(vertex, []) if v not in visited])
        return result

    def dfs(self, start):
        """Performs a depth-first search starting from the given vertex."""
        visited = set()
        stack = [start]
        result = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                stack.extend([v for v in self.adj_list.get(vertex, []) if v not in visited])
        return result

# Example Usage
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "A")

print("BFS starting from A:", graph.bfs("A"))
print("DFS starting from A:", graph.dfs("A"))
