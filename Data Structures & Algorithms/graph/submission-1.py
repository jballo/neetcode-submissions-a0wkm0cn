from collections import deque

class Graph:
    
    def __init__(self):
        self.verteces = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.verteces:
            self.verteces[src] = set()
        if dst not in self.verteces:
            self.verteces[dst] = set()

        self.verteces[src].add(dst)
        # if dst not in self.verteces[src]:

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.verteces:
            return False
        if dst not in self.verteces:
            return False

        if dst not in self.verteces[src]:
            return False

        self.verteces[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        # dfs approach, but bfs will be more optimal
        visited = set()
        queue = deque()
        visited.add(src)
        queue.append(src)

        while queue:
            for i in range(len(queue)):
                vertex = queue.popleft()
                if vertex == dst:
                    return True
                
                for neigh in self.verteces[vertex]:
                    if neigh in visited:
                        continue
                    visited.add(neigh)
                    queue.append(neigh)

        
        return False

