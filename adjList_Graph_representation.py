class graph:
    def __init__(self):
        self.adjList = {}
    
    def add_vertex(self,vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = []
    
    def add_edge(self,scr,dest):
        self.add_vertex(scr)
        self.add_vertex(dest)

        self.adjList[scr].append(dest)
        self.adjList[dest].append(scr)

    def print(self):
        for vertex in self.adjList:
            print(vertex, "->", self.adjList[vertex], end = "\n")
G = graph()
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(1,4)
G.add_edge(4,3)
G.add_edge(2,4)
G.add_edge(4,5)
G.add_edge(3,5)
G.print()