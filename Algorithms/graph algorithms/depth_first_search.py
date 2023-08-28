class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, neighbor):
        if vertex not in self.graph:
            self.graph[vertex] = []
        self.graph[vertex].append(neighbor)

    def dfs(self, vertex, visited=None):
        if visited is None:
            visited = set()

        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)

            for neighbor in self.graph.get(vertex, []):
                self.dfs(neighbor, visited)

# Creating a graph
my_graph = Graph()

# Adding edges
my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("B", "D")
my_graph.add_edge("B", "E")
my_graph.add_edge("C", "F")

# Perform DFS starting from vertex "A"
print("DFS traversal starting from 'A':")
my_graph.dfs("A")
