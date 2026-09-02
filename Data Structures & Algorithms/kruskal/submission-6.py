import heapq

class Union:
    def __init__(self, n):
        self.parents = []
        self.rank = []
        for i in range(n):
            self.parents.append(i)

        for i in range(n):
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

        if self.rank[px] > self.rank[py]:
            self.parents[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parents[px] = py
        else:
            self.parents[py] = px
            self.rank[px] += 1
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:

        # graph = {}
        # for i in range(n):
        #     graph[i] = []

        
        # for src, dst, weight in edges:
        #     graph[src].append((dst, weight))
        #     graph[dst].append((src, weight))


        struct = Union(n)

        minHeap = []

        for src, dst, weight in edges:
            heapq.heappush(minHeap, (weight, src, dst))
        
        visited = 0
        total = 0
        while minHeap and visited < n:
            w, s, d = heapq.heappop(minHeap)
            print('compare')
            print("w: ", w)
            print("s: ", s)
            print("d: ", d)

            if not struct.union(s, d):
                continue

            visited += 1
            total += w

        print("visited: ", visited)
        print("total: ", total)

        return total if visited == n - 1 else -1
