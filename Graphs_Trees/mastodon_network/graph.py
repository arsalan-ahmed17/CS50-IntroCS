from typing import List, Tuple, Optional, Union
import json
import itertools
import graphviz
import os


class User():
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username


class Graph(dict):
    """
    A graph object based on a dictionary implementation.

    Attributes:
    ----------
    sps: n*n (2-dimensional) matrix to store shortest paths between all nodes

    Methods:
    ----------
    add_vertex()
    """
    def __init__(self) -> None:
        """
        Initialize the Graph object as an empty dictionary.
        """
        super().__init__()
        self.sps = None  # Shortest path matrix, initialized as None

    def add_vertex(self, user: object) -> None:
        key = str(user)
        if key not in self:
            self[key] = []

        """
        Adds a vertex to the graph.

        Parameters:
        ----------
        user: The user object or identifier to be added as a vertex.
        """
        # Use the string representation of the user as the key
        pass

    def add_edge(self, origin: object, target: object) -> None:
        """
        Adds an edge to the graph between `origin` and `target`.

        Parameters:
        ----------
        origin: The originating vertex.
        target: The target vertex.
        """

        key_origin = str(origin)
        key_target = str(target)

        # Ensure both vertices exist in the graph.
        if key_origin not in self:
            self.add_vertex(origin)
        if key_target not in self:
            self.add_vertex(target)

        # Add the edge from origin to target if it doesn't exist.
        if key_target not in self[key_origin]:
            self[key_origin].append(key_target)
            self[key_origin].sort()  # Keep the neighbors sorted alphabetically.

        # Since the graph is undirected, add the edge from target to origin as well.
        if key_origin not in self[key_target]:
            self[key_target].append(key_origin)
            self[key_target].sort()
            pass

    def remove_edge(self, edge: Tuple[object, object]) -> None:
        """
        Removes an edge from the graph.

        Parameters:
        ----------
        edge: Tuple containing the vertices that form the edge.
        """

        origin, target = edge
        key_origin = str(origin)
        key_target = str(target)

        # Remove target from origin's neighbor list if it exists.
        if key_origin in self and key_target in self[key_origin]:
            self[key_origin].remove(key_target)

        # Remove origin from target's neighbor list if it exists.
        if key_target in self and key_origin in self[key_target]:
            self[key_target].remove(key_origin)
        pass

    def remove_vertex(self, user: object) -> None:
        """
        Removes a vertex and all its edges from the graph.

        Parameters:
        ----------
        user: The user object or identifier to be removed.
        """
        key = str(user)

        if key in self:
            # Remove this vertex from all of its neighbors' lists.
            for neighbor in list(self[key]):  # Use a copy since we'll modify the list.
                if neighbor in self and key in self[neighbor]:
                    self[neighbor].remove(key)
            # Finally, remove the vertex from the graph.
            del self[key]
        pass

    def dfs(self, start: object) -> List[str]:
        """
        Performs a pre-order depth-first search starting at 'start'.
        Returns the list of visited vertices.
        """
        start_key = str(start)
        visited = []  # List to record the order of visited nodes

        def _dfs(v: str):
            if v not in visited:
                visited.append(v)
                # Since our neighbor lists are sorted, this will traverse alphabetically.
                for neighbor in self.get(v, []):
                    _dfs(neighbor)

        _dfs(start_key)
        return visited
        pass
    def get_subgraphs(self) -> List[List[str]]:
        """
        Finds disconnected subgraphs (clusters) in the graph.

        Returns:
        ----------
        List of subgraphs, where each subgraph is a list of vertices.
        """

        all_vertices = set(self.keys())
        visited = set()
        subgraphs = []

        # Iterate over vertices in sorted order for consistency.
        for vertex in sorted(all_vertices):
            if vertex not in visited:
                # Run DFS starting at this vertex to get all connected vertices.
                component = self.dfs(vertex)
                subgraphs.append(component)
                visited.update(component)
        return subgraphs
        pass

    def shortest_path(self, start: object, end: object) -> Union[List[str],None]:
        """
        Breadth-first search from `start` to `end` with path tracking to identify the shortest path.

        Parameters:
        ----------
        start: The starting vertex.
        end: The end vertex.

        Returns:
        ----------
        List of vertices forming the shortest path from start to end, or None if there is no path.
        """
        start_key = str(start)
        end_key = str(end)

        # If one of the vertices is missing, there is no path.
        if start_key not in self or end_key not in self:
            return None

        from collections import deque
        queue = deque([[start_key]])
        visited = {start_key}

        while queue:
            path = queue.popleft()
            current = path[-1]
            if current == end_key:
                return path
            for neighbor in self.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [neighbor]
                    queue.append(new_path)
        return None
        pass

    def most_influential(self) -> Tuple[str, float]:
        """
        Identifies the most influential user based on average shortest path length.

        Returns:
        ----------
        Tuple containing the most influential user and its average shortest path length.
        """
        if not self:
            return []

        vertices = list(self.keys())
        influence = {}

        # For each vertex, compute the average shortest path length to all others.
        for v in vertices:
            total_length = 0
            reachable_count = 0
            for u in vertices:
                if u != v:
                    sp = self.shortest_path(v, u)
                    if sp:  # Only consider if a path exists
                        total_length += len(sp)
                        reachable_count += 1
            # If no other vertices are reachable, assign infinite average.
            avg_length = total_length / reachable_count if reachable_count > 0 else float('inf')
            influence[v] = avg_length

        # Find the minimum average value.
        min_avg = min(influence.values())
        # Return all vertices whose average shortest path equals the minimum.
        return [(v, influence[v]) for v in vertices if influence[v] == min_avg]
        # Initialize a matrix to store shortest paths between all possible node combinations
	# (including those with 'None' values)

        # Populate the matrix with shortest paths between all possible node combinations

        # Calculate the average shortest path length for each node

        # Identify the most influential node based on minimum average shortest path length and return both


    def edge_in_sp(self, pair: Tuple[str, str], sp: List[str]) -> bool:
        """
        Checks if an edge exists in the given shortest path.

        Parameters:
        ----------
        pair: Tuple containing the users that form the edge.
        sp: The shortest path, represented as a list of vertices.

        Returns:
        ----------
        Boolean value indicating the presence of the edge in the shortest path.
        """
        if not sp or len(sp) < 2:
            return False
        a, b = pair
        for i in range(len(sp) - 1):
            # Check both orders.
            if (sp[i] == a and sp[i + 1] == b) or (sp[i] == b and sp[i + 1] == a):
                return True
        return False

    def compute_sps(self) -> None:
        """
        Computes shortest paths between every pair of nodes and stores them in `self.sps`.
        """
        vertices = sorted(self.keys())  # Get vertices in a consistent order.
        self._vertex_order = vertices     # Save the order for later use.
        n = len(vertices)
        self.sps = []  # This will be our n x n matrix.

        for i in range(n):
            row = []
            for j in range(n):
                if i == j:
                    # The shortest path from a vertex to itself is just a list containing that vertex.
                    row.append([vertices[i]])
                else:
                # Use your existing shortest_path method.
                    sp = self.shortest_path(vertices[i], vertices[j])
                    row.append(sp)
            self.sps.append(row)

    def edge_to_remove(self) -> Tuple[str, str]:
        """
        Identifies the edge to remove based on edge betweenness.

        Returns:
        ----------
        Tuple containing the vertices of the edge to remove.
        """
        # Ensure that the vertex order is defined.
        if not hasattr(self, '_vertex_order'):
            self.compute_sps()

        order = self._vertex_order
        # our consistent ordering of vertices

        edge_betweenness = {}
        seen_edges = set()

        # Gather unique edges from the graph.
        for u in order:
            for v in self[u]:
                # Use a sorted tuple to ensure each edge is only considered once.
                edge = tuple(sorted([u, v]))
                seen_edges.add(edge)

        # Compute betweenness for each edge.
        for edge in seen_edges:
            count = 0
            for i, source in enumerate(order):
                for j, target in enumerate(order):
                    # Consider each unordered pair only once.
                    if source < target:
                        sp = self.sps[i][j]  # use integer indices into the matrix
                        if sp and self.edge_in_sp(edge, sp):
                            count += 1
            edge_betweenness[edge] = count

        # If no edges exist, return None.
        if not edge_betweenness:
            return None

        # Return the edge with the highest betweenness.
        return max(edge_betweenness, key=edge_betweenness.get)

    def girvan_newman_algorithm(self, clusters: int) -> List[List[str]]:
        """
        Applies the Girvan-Newman algorithm to decompose the graph into specified
        number of clusters (disconnected subgraphs).

        Pseudocode for the Girvan-Newman algorithm:
        -------------------------------------------
        1. Calculate the betweenness of all existing edges in the mastodon_network.
        2. Remove the edge with the highest betweenness.
        3. Calculate the number of disconnected subgraphs.
        4. Repeat steps 1-3 until the number of disconnected subgraphs equals the predefined number of clusters.

        Parameters:
        ----------
        clusters: The number of clusters to decompose the graph into.

        Returns:
        ----------
        List of clusters, where each cluster is a list of vertices.
        """
        current_subgraphs = self.get_subgraphs()
        # Continue removing edges until we have the desired number of clusters.
        while len(current_subgraphs) < clusters or (len(current_subgraphs) == 1 and len(current_subgraphs[0]) == len(self)):
            # If we've reached or exceeded the desired number of clusters, break.
            if len(current_subgraphs) >= clusters:
                break

            # Recompute all shortest paths after the latest change.
            self.compute_sps()
            # Identify the edge to remove.
            edge = self.edge_to_remove()
            if not edge:
                break  # No removable edge remains.
            self.remove_edge(edge)
            # Update the list of clusters.
            current_subgraphs = self.get_subgraphs()

        return current_subgraphs

    def parse_data(self, filepath: str = 'ressources/graph_52n.json') -> None:
        """
        Parses graph data from a JSON file and populates the graph.

        Parameters:
        ----------
        filepath: Path to the JSON file containing the graph data.
        """
        # Open and read the JSON file
        with open(filepath, 'r') as file:
            data = json.load(file)

        # Remove the first key-item pair from data (if applicable)
        if data:
            first_key = list(data.keys())[0]
            del data[first_key]

        # Iterate over the data to populate vertices and edges
        for key, neighbors in data.items():
            key_user = User(key)

            # Add vertex for the user represented by 'key'
            self.add_vertex(key_user)

            # Add edges between 'key' and its neighbors
            for neighbor in neighbors:
                neighbor_user = User(neighbor)
                self.add_edge(key_user, neighbor_user)

    def show(self) -> None:
        """
        Generates and displays a visual representation of the graph.
        """
        # Initialize a Graphviz graph
        graph = graphviz.Graph(format='png', strict=True, filename='')

        # Add nodes to the Graphviz graph
        for node in self.keys():
            graph.node(str(node), str(node))

        # Add edges to the Graphviz graph
        for node in self.keys():
            for target in self[node]:
                graph.edge(str(node), str(target))

        # Render the graph and create a PNG file
        graph.render()

        # Remove temporary files if needed
        os.remove('')
