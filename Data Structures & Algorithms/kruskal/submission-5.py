import heapq
class Union:

    def __init__(self, n):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 1
    
    def find(self, n):

        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n

    def union(self, x, y):
        parX, parY = self.find(x), self.find(y)
        if parX == parY:
            return False

        if self.rank[parX] < self.rank[parY]:
            self.par[parX] = parY
        elif self.rank[parX] > self.rank[parY]:
            self.par[parY] = parX
        else:
            self.par[parY] = parX
            self.rank[parY] += 1
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []
        for u, v, w in edges:
            heapq.heappush(minHeap, (w, u, v))
        
        totalWeight = 0
        unionDst = Union(n)

        edges = 0
        while minHeap:
            weight, src, dst = heapq.heappop(minHeap)
            if not unionDst.union(src, dst):
                continue
            
            totalWeight += weight
            edges += 1
            
        return totalWeight if edges == n - 1 else -1

