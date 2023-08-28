class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def display(self):
        for vertex in self.graph:
            print(vertex, "->", " -> ".join(str(neighbour) for neighbour in self.graph[vertex]))

# Creating a graph
my_graph = Graph()

# Adding vertices
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")

# Adding edges
my_graph.add_edge("A", "B")
my_graph.add_edge("B", "C")
my_graph.add_edge("C", "D")
my_graph.add_edge("D", "A")

# Displaying the graph
my_graph.display()
