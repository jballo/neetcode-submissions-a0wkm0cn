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
        pX, pY = self.find(x), self.find(y)

        if pX == pY:
            return False
        
        if self.rank[pX] < self.rank[pY]:
            self.par[pX] = pY
        elif self.rank[pX] > self.rank[pY]:
            self.par[pY] = pX
        else:
            self.par[pY] = pX
            self.rank[pX] += 1
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        rep = {}
        minHeap = []
        for i in range(len(points)):
            rep[(points[i][0], points[i][1])] = i
        

        edges = 0
        totalWeight = 0
        unionDst = Union(len(points))
        for j in range(len(points)):
            for i in range(len(points)):
                if i == j:
                    continue
                mX = abs(points[j][0] - points[i][0])
                mY = abs(points[j][1] - points[i][1])
                m = mX + mY
                heapq.heappush(minHeap, (m, rep[points[j][0], points[j][1]], rep[points[i][0], points[i][1]]))
        
        while minHeap and edges < len(points) -1:
            w, src, dst = heapq.heappop(minHeap)
            if not unionDst.union(src, dst):
                continue
            
            edges += 1
            totalWeight += w

        return totalWeight if edges == len(points) - 1 else -1
        
