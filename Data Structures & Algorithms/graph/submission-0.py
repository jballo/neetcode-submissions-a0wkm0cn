from collections import deque

class Graph:
    
    def __init__(self):
        self.verteces = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.verteces:
            self.verteces[src] = set()
        if dst not in self.verteces:
            self.verteces[dst] = set()
        if dst not in self.verteces[src]:
            self.verteces[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.verteces:
            return False
        
        if dst not in self.verteces[src]:
            return False
        
        self.verteces[src].remove(dst)
        return True
        
        

    def hasPath(self, src: int, dst: int) -> bool:

        if src not in self.verteces:
            return False
    
        # If dst doesn't exist, it can't be reached
        if dst not in self.verteces:
            return False
        visited = set()
        queue = deque()
        queue.append(src)
        visited.add(src)

        while queue:
            for i in range(len(queue)):
                vertex = queue.popleft()
                if vertex == dst:
                    return True
                
                for neighbour in self.verteces[vertex]:
                    if neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)
        

        return False       
        
