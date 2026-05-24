class Union:
    def __init__(self, n):
        self.parents = [r for r in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, n):
        while n != self.parents[n]:
            self.parents[n] = self.parents[self.parents[n]]
            n = self.parents[n]
        return n
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if self.rank[px] > self.rank[py]:
            self.parents[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parents[px] = py
        else:
            self.parents[py] = px
            self.rank[px] += 1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        unionStruct = Union(len(edges))

        for x,y in edges:
            if unionStruct.find(x) == unionStruct.find(y):
                return [x,y]
            
            unionStruct.union(x,y)
        




