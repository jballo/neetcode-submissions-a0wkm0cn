class UnionFind:
    
    def __init__(self, n: int):
        self.parents = [r for r in range(n)]
        self.rank = [0] * n

    def find(self, x: int) -> int:
        while x != self.parents[x]:
            x = self.parents[x]
        return x

    def isSameComponent(self, x: int, y: int) -> bool:
        px = self.find(x)
        py = self.find(y)
        return True if px == py else False

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)

        if px == py:
            return False

        if self.rank[px] > self.rank[py]:
            self.parents[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parents[px] = py
        else:
            self.parents[py] = px
            self.rank[px] += 1
        return True

    def getNumComponents(self) -> int:
        componentSet = set()
        for i in range(len(self.parents)):
            pi = self.find(i)
            if pi not in componentSet:
                componentSet.add(pi)       

        return len(componentSet)
