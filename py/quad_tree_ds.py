# Quad Tree Data Structure

## 1. Concept Overview

"""
A Quad Tree is a tree data structure in which each internal node has exactly four children. It is primarily used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions. This structure is especially useful in applications involving spatial indexing, such as image compression, spatial databases, and computer graphics.

The fundamental idea is to divide the space into four quadrants at each level of the tree. Each node in the Quad Tree represents a specific region of the space, and the four children of a node correspond to the four quadrants of that region. This allows for efficient querying and updating of spatial data by limiting the search space at each level of the tree.
"""

## 2. Implementation Details

"""
The implementation of a Quad Tree involves defining a node structure that contains data about the spatial region it represents, pointers to its four children (representing the four quadrants), and potentially a list of points or data items stored within that region.

A Quad Tree is typically constructed with the following components:
- A root node representing the entire space.
- Each node stores the boundaries of its region.
- Each internal node divides its region into four quadrants, each associated with a child node.
- Leaf nodes contain actual data points or references to data items.

The construction of the tree is recursive, where each node divides its region until a specified level of granularity is reached (e.g., a maximum depth or a minimum number of points per node).
"""

## 3. Core Operations & Time Complexities

"""
Core operations of a Quad Tree include:

1. Insertion:
   - Insert a point or data item into the tree by identifying the appropriate quadrant.
   - Time Complexity: O(log(n)) on average, depending on the depth and balance of the tree.

2. Deletion:
   - Remove a point or data item by locating it within the tree and adjusting the node structure as necessary.
   - Time Complexity: O(log(n)) on average.

3. Query:
   - Retrieve points or data items within a specified region.
   - Time Complexity: O(log(n) + k), where k is the number of points in the result set.

4. Subdivision:
   - Split a node into four children when it reaches a predefined capacity or depth.
   - Time Complexity: O(1) for the subdivision.

These operations leverage the spatial partitioning nature of the Quad Tree to efficiently manage and access spatial data.
"""

## 4. Common Use Cases

"""
Quad Trees are commonly used in the following scenarios:

- Spatial indexing in geographical information systems (GIS) for efficient querying.
- Image compression techniques, such as in the representation of sparse images.
- Collision detection in computer graphics and gaming, where spatial partitioning helps in determining potential collisions efficiently.
- Efficient storage and retrieval of spatial data in databases.
"""

## 5. Trade-offs

"""
Trade-offs associated with Quad Trees include:

- Balance: Quad Trees can become unbalanced if data points are unevenly distributed, leading to inefficient operations.
- Overhead: The recursive subdivision can lead to significant overhead in terms of memory and processing, especially for sparse data.
- Complexity: Implementing an efficient Quad Tree requires careful consideration of region boundaries and node management, which can complicate the design.
"""

## 6. Design Decisions

"""
Key design decisions when implementing a Quad Tree include:

- Defining the criteria for subdividing nodes, such as a maximum depth or a minimum number of points per node.
- Choosing an appropriate representation for regions (e.g., bounding boxes) and points.
- Deciding on the balance between depth and breadth of the tree to optimize performance for specific use cases.
"""

## 7. Visual / Intuition

"""
Visual intuition for a Quad Tree can be gained by imagining a 2D space that is recursively divided into four quadrants. Each node in the tree represents a region of this space, with its children representing the four quadrants of that region. This hierarchical structure allows for efficient spatial partitioning and querying.
"""

## 8. Programming Patterns

"""
Programming patterns in Quad Trees often involve recursion for tree traversal and node management. Common patterns include:

- Recursive insertion and deletion of points by navigating the tree structure to locate the appropriate region.
- Depth-first search for querying points within a specific region.
- Recursive subdivision of nodes to maintain the tree's structure and balance.
"""

## 9. Typical Problems

"""
Typical problems addressed by Quad Trees include:

- Efficiently managing and querying large sets of spatial data.
- Implementing collision detection systems in gaming and simulations.
- Compressing and representing sparse images or spatial data efficiently.
"""

## 10. Gotchas / Pitfalls

"""
- Handling edge cases where points lie on the boundaries of regions.
- Managing the balance of the tree to prevent skewed structures.
- Dealing with overlapping regions, especially in cases of deletion and subdivision.
"""

## 11. Code Implementation (Demo of Core Operations)

"""
Below is a sample implementation of a Quad Tree in Python, demonstrating core operations like insertion and querying.
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class QuadTreeNode:
    def __init__(self, boundary, capacity):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def subdivide(self):
        x, y, w, h = self.boundary
        nw = (x, y, w/2, h/2)
        ne = (x + w/2, y, w/2, h/2)
        sw = (x, y + h/2, w/2, h/2)
        se = (x + w/2, y + h/2, w/2, h/2)
        self.northwest = QuadTreeNode(nw, self.capacity)
        self.northeast = QuadTreeNode(ne, self.capacity)
        self.southwest = QuadTreeNode(sw, self.capacity)
        self.southeast = QuadTreeNode(se, self.capacity)
        self.divided = True

    def insert(self, point):
        if not self.contains(self.boundary, point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        else:
            if not self.divided:
                self.subdivide()

            if self.northwest.insert(point):
                return True
            elif self.northeast.insert(point):
                return True
            elif self.southwest.insert(point):
                return True
            elif self.southeast.insert(point):
                return True

        return False

    def contains(self, boundary, point):
        x, y, w, h = boundary
        return (x <= point.x < x + w) and (y <= point.y < y + h)

    def query(self, range, found):
        if not self.intersects(self.boundary, range):
            return
        else:
            for p in self.points:
                if self.contains(range, p):
                    found.append(p)

            if self.divided:
                self.northwest.query(range, found)
                self.northeast.query(range, found)
                self.southwest.query(range, found)
                self.southeast.query(range, found)

    def intersects(self, boundary, range):
        x, y, w, h = boundary
        rx, ry, rw, rh = range
        return not (rx > x + w or rx + rw < x or ry > y + h or ry + rh < y)

# Example usage:
boundary = (0, 0, 200, 200)
qt = QuadTreeNode(boundary, 4)

qt.insert(Point(50, 50))
qt.insert(Point(150, 150))

found_points = []
qt.query((0, 0, 100, 100), found_points)

for p in found_points:
    print(f"Point found at ({p.x}, {p.y})")
