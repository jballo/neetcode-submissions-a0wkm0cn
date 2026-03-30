class Graph:
    
    def __init__(self):
        self.verteces = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.verteces:
            self.verteces[src] = []
        if dst not in self.verteces:
            self.verteces[dst] = []

        self.verteces[src].append(dst)

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
        from collections import deque 

        visited = set()
        queue = deque()
        visited.add(src)
        queue.append(src)

        while queue:
            for i in range(0, len(queue)):
                vertex = queue.popleft()

                if vertex == dst:
                    return True
                
                for vert in self.verteces[vertex]:
                    if vert in visited:
                        continue

                    queue.append(vert)
                    visited.add(vert)
        
        return False




