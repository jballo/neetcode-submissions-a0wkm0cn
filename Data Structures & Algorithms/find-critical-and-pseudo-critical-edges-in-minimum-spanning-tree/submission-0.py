import heapq
class Union:
    def __init__(self, n):
        self.parents = []
        self.rank = []
        for i in range(n):
            self.parents.append(i)
            self.rank.append(1)

    def find(self, n):
        while n != self.parents[n]:
            self.parents[n] = self.parents[self.parents[n]]
            n = self.parents[n]
        return n

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            self.parents[px] = py
            self.rank[py] += self.rank[px]
        elif self.rank[px] > self.rank[py]:
            self.parents[py] = px
            self.rank[px] += self.rank[py]

        else:
            self.parents[py] = px
            self.rank[px] += self.rank[py]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        mstWeight = 0
        minHeap = []
        uf = Union(n)
        for u, v, c, in edges:
            heapq.heappush(minHeap, (c, u, v))

        while minHeap:
            c, u, v = heapq.heappop(minHeap)
            if not uf.union(u, v):
                continue
            mstWeight += c
        
        critical = []
        pseudo = []

        for i in range(len(edges)):
            # check if its critical - build a mst without 
            wUF = Union(n)
            minHeapWithout = []
            mstWeightWithout = 0
            for j in range(len(edges)):
                if j == i:
                    continue
                u, v, c = edges[j][0], edges[j][1], edges[j][2]
                heapq.heappush(minHeapWithout, (c, u, v))
            
            while minHeapWithout:
                c, u, v = heapq.heappop(minHeapWithout)
                if not wUF.union(u, v):
                    continue
                mstWeightWithout += c
            
            if max(wUF.rank) != n or mstWeightWithout > mstWeight:
                critical.append(i)
                continue

            nUf = Union(n)
            minHeapWith = []
            mstWeightWith = edges[i][2]
            nUf.union(edges[i][0], edges[i][1])

            for j in range(len(edges)):
                u, v, c = edges[j][0], edges[j][1], edges[j][2]
                heapq.heappush(minHeapWith, (c, u, v))

            while minHeapWith:
                c, u, v = heapq.heappop(minHeapWith)
                if not nUf.union(u, v):
                    continue
                mstWeightWith += c

            if mstWeightWith == mstWeight:
                pseudo.append(i)
        
        return [critical, pseudo]

            # check if its pseudocritical
            
