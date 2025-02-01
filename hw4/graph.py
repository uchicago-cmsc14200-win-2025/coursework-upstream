"""
CMSC 14200, Winter 2025
Homework #4

Grid Graph implementation

DO NOT MODIFY THIS FILE
"""
import random
import json

from typing import Any

class Vertex:
    """
    Class to represent a vertex in a directed, weighted graph
    """

    __name: str
    __attributes: dict[str, Any]
    __out_edges: dict[str, "Edge"]
    
    def __init__(self, name: str):
        """
        Constructor

        Parameters:
            name [str]: identifier for the vertex
        """
        self.__name = name
        self.__out_edges = {}
    
    @property
    def name(self) -> str:
        """
        Get the name of a vertex

        Parameters: none beyond self

        Returns [str]: the name
        """
        return self.__name
    

    
    def add_out_edge(self, edge: "Edge") -> None:
        """
        Add an outgoing edge to the vertex

        Parameters:
            edge [Edge]: the edge to add

        Returns: nothing
        
        Raises:
            ValueError: if the edge has a different origin
        """
        if edge.origin is not self:
            raise ValueError("adding edge out of vertex with different origin")
        dest_name = edge.destination.name
        
        if dest_name not in self.__out_edges:
            self.__out_edges[dest_name] = edge
    
    @property
    def out_neighbors(self) -> set[str]:
        """
        Finds the set of vertex identifiers for vertices to which this vertex
            has outgoing edges

        Parameters: none beyond self

        Returns [set[str]]: the set of neighbors' vertex identifiers
        """
        return set(self.__out_edges.keys())
    
    def get_edge_to(self, destination: str) -> "Edge|None":
        """
        Find the edges from this vertex to another specified vertex

        Parameters:
            destination [str]: the destination vertex's identifier

        Returns [[Edge]]: the edges from this vertex to the
            destination
        """
        return self.__out_edges.get(destination,None)
    
    def __repr__(self) -> str:
        """
        Generate a string representation of this vertex

        Parameters: none beyond self

        Returns [str]: a string representation
        """
        return f"Vertex({self.__name},\n\t[{self.__out_edges}])"

class Edge:
    """
    Class to represent an edge in a directed, weighted graph
    """

    __origin: Vertex
    __destination: Vertex
    __weight: int
    
    def __init__(self, origin: Vertex, destination: Vertex, weight: int):
        """
        Constructor

        Parameters:
            origin [Vertex]: origin vertex of the edge
            destination [Vertex]: destination vertex of the edge
            weight [int]: weight of the edge
        """
        self.__origin = origin
        self.__destination = destination
        assert weight >= 0, "Negative Edge Weights are Not Allowed!"
        self.__weight = weight
        
    @property
    def origin(self) -> Vertex:
        """
        Get the origin of the edge

        Parameters: none beyond self

        Returns [Vertex]: the origin vertex
        """
        return self.__origin
    
    @property
    def destination(self) -> Vertex:
        """
        Get the destination vertex of the edge

        Parameters: none beyond self

        Returns [Vertex]: the destination vertex
        """
        return self.__destination
    
    @property
    def weight(self) -> int:
        """
        Get the weight of the edge

        Parameters: none beyond self

        Returns [int]: the weight
        """
        return self.__weight

    def __str__(self) -> str:
        """
        Generate a string representation of this edge

        Parameters: none beyond self

        Returns [str]: a string representation
        """
        return f"Edge({self.__origin.name} --{self.__weight}--> " + \
               f"{self.__destination.name})"
    

class GridGraph:
    """
    Class to represent a directed, weighted grid graph
    """

    __vertices: list[list[Vertex]]
    __vertex_dict: dict[str, Vertex]
    M: int
    N: int
    
    def __init__(self) -> None:
        """
        Constructor

        Parameters: M (int) - No of rows in the grid
                    N (int) - No of columns in the grid
        """
        # Initialize the grid graph
        self.M = 0
        self.N = 0
        self.__vertices = []
        self.__vertex_dict = {}

    def validate_dimensions(self) -> None:
        """
        Validate the dimensions of the grid graph

        Parameters: none beyond self

        Returns: nothing
        
        Raises:
            ValueError: if the dimensions are invalid
        """
        if self.M < 1 or self.N < 1:
            raise ValueError("invalid dimensions")
        elif self.M * self.N > 26:
            raise ValueError("The total number of nodes (MxN) cannot exceed 26!")


    def save_graph(self, filename: str) -> None:
        """
        Save the graph to a file

        Parameters:
            filename [str]: the file to which to save the graph

        Returns: nothing
        """
        grid = []

        for row in self.__vertices:
            out_row = []
            for vertex in row:
                out_edge_d = {}
                for n in vertex.out_neighbors:
                    dest = vertex.get_edge_to(n)
                    assert isinstance(dest, Edge)
                    out_edge_d[n] = dest.weight
                out_row.append({"name": vertex.name, "out_edges": out_edge_d})      
            grid.append(out_row)

        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump({'M': self.M, 'N': self.N, 'grid': grid}, fp)
        
        
    def load_graph(self, filename: str) -> None:
        """
        Load a graph into the grid

        Parameters:
            filename [str]: The JSON file containing the graph to be loaded

        Returns: nothing
        """
        with open(filename, 'r') as fp:
            graph_dict = json.load(fp)

        self.M = graph_dict['M']
        self.N = graph_dict['N']
        self.__vertices = []
        self.__vertex_dict = {}

        self.validate_dimensions()

        for i in range(self.M):
            row = []
            for j in range(self.N):
                v_dict = graph_dict['grid'][i][j]
                v = Vertex(v_dict['name'])
                row.append(v)
                self.__vertex_dict[v.name] = v
            self.__vertices.append(row)

        for i in range(self.M):
            for j in range(self.N):
                src = self.get_by_pos(i,j)
                v_dict = graph_dict['grid'][i][j]
                for name in v_dict['out_edges']:
                    dest = self.get_by_name(name)
                    src.add_out_edge(Edge(src, dest, v_dict['out_edges'][name]))

    def generate_random_graph(self, M: int, N: int) -> None:
        """Generate a MxN grid of vertices for the game."""

        # Reset the vertices
        self.__vertices = []
        self.__vertex_dict = {}
        self.M = M
        self.N = N

        self.validate_dimensions()

        available_names = [chr(ord("A") + i) for i in range(26)]

        for i in range(self.M):
            row = []
            for j in range(self.N):
                rand_index = random.randint(0, len(available_names) - 1)
                v_name = available_names.pop(rand_index)
                v = Vertex(v_name)
                row.append(v)
                self.__vertex_dict[v.name] = v
            self.__vertices.append(row)

        for i in range(self.M):
            for j in range(self.N):
                src = self.get_by_pos(i,j)
                destinations = []
                if j < self.N - 1:
                    # Add edges to the right vertex and vice-versa
                    destinations.append(self.get_by_pos(i, j+1))
                if i < self.M - 1:
                    # Add edge to the bottom vertex and vice-versa
                    destinations.append(self.get_by_pos(i + 1,j))
                if i < self.M - 1 and j < self.N - 1:
                    # Add edge to the bottom-right and vice-versa
                    destinations.append(self.get_by_pos(i + 1,j + 1))
                if i < self.M - 1 and j > 0:
                    # Add edge to the bottom-left and vice-versa
                    destinations.append(self.get_by_pos(i + 1,j - 1))

                for dest in destinations:
                    weight = random.randint(1,99)
                    src.add_out_edge(Edge(src,dest,weight))
                    dest.add_out_edge(Edge(dest,src,weight))

    def get_by_pos(self, i: int, j: int) -> Vertex:
        return self.__vertices[i][j]
    
    def get_by_name(self, name: str) -> Vertex:
        return self.__vertex_dict[name]
    
    def weight_by_pos(self, src: tuple[int,int], dest: tuple[int,int]) -> int:
        """Return the weight of the edge from src to dest."""

        src_v = self.get_by_pos(src[0],src[1])
        dest_v = self.get_by_pos(dest[0],dest[1])

        edge = src_v.get_edge_to(dest_v.name)
        if not edge:
            raise ValueError("no edge from src to dest")
        return edge.weight
    
    def weight_by_name(self, src: str, dest: str) -> int:
        """Return the weight of the edge from src to dest."""

        src_v = self.get_by_name(src)
        dest_v = self.get_by_name(dest)
        
        edge = src_v.get_edge_to(dest_v.name)
        if not edge:
            raise ValueError("no edge from src to dest")
        return edge.weight
    
    @property
    def render_graph(self) -> str:
        """Render the graph in a grid-like format in ASCII"""

        render = ""

        node = "[{}]"
        hor_edge = "--{:02d}---"
        ver_edge_1 = "| \\     / "
        ver_edge_2 = "| {:02d}  {:02d}  "
        ver_edge_2 = "| {:02d}  {:02d}  "
        ver_edge_3 = "{:02d}  \\/    "
        ver_edge_4 = "|   /\\    "
        ver_edge_4 = "|   /\\    "
        ver_edge_5 = "| /    \\  "

        end_edge = "|"
        ver_edge = "{:02d}"

        for i in range(self.M):
            # Print the first line (contains the nodes)
            line = ""
            for j in range(self.N):
                # Print the first Line
                line += node.format(self.get_by_pos(i,j).name)
                if j < self.N - 1:
                    line += hor_edge.format(self.weight_by_pos((i, j), (i, j + 1)))
            render += line + "\n"

            if i < self.M -1:
                # Print the second line
                line = ""
                for j in range(self.N-1):
                    line += ver_edge_1
                line += end_edge
                render += line + "\n"

                # Print the third line
                line = ""
                for j in range(self.N):
                    if j < self.N - 1:
                        line += ver_edge_2.format(self.weight_by_pos((i, j), (i+1, j+1)), self.weight_by_pos((i, j+1), (i+1, j)))
                    else:
                        line += end_edge
                render += line + "\n"

                # Print the fourth line
                line = ""
                for j in range(self.N):
                    if j < self.N - 1:
                        line += ver_edge_3.format(self.weight_by_pos((i, j), (i+1, j)))
                    else:
                        line += ver_edge.format(self.weight_by_pos((i, j), (i+1, j)))
                render += line + "\n"
                # Print the fifth line
                line = ""
                for j in range(self.N-1):
                    line += ver_edge_4.format(self.weight_by_pos((i, j+1), (i+1, j)))
                line += end_edge
                render += line + "\n"

                # Print the sixth line
                line = ""
                for j in range(self.N-1):
                    line += ver_edge_5
                line += end_edge
                render += line + "\n"

        return render
        
    @property
    def vertices(self) -> set[str]:
        """
        Get the set of vertex identifiers in the graph

        Parameters: none beyond self

        Returns [set[str]]: the set of vertex identifiers
        """
        return set(self.__vertex_dict.keys())
    
    def __repr__(self) -> str:
        """
        Generate a string representation of the graph

        Parameters: none beyond self

        Returns [str]: a string representation
        """
        return f"GridGraph: {self.M}x{self.N}"
