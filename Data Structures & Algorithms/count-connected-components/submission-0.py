class Union:
    def __init__(self, n):
        self.parents = [r for r in range(n)]
        self.ranks = [1] * n
        self.componentCount = n

    def find(self, n):
        while n != self.parents[n]:
            self.parents[n] = self.parents[self.parents[n]]
            n = self.parents[n]
        return n

    # 5
    # 4
    # 3
    # 2
    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False
        
        if self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        elif self.ranks[px] < self.ranks[px]:
            self.parents[px] = py
        else:
            self.parents[py] = px
            self.ranks[px] += 1
        self.componentCount -= 1
        return True

        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        connections = Union(n)

        for i in range(len(edges)):
            connections.union(edges[i][0], edges[i][1])
        
        return connections.componentCount



