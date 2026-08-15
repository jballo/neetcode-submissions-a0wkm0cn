import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        shortest = {}

        for i in range(n):
            shortest[i] = -1

        graph = {}
        for u, v, w in edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []

            graph[u].append((v, w))


        minHeap = [(0, src)]

        while minHeap:
            w, u = heapq.heappop(minHeap)

            if shortest[u] != -1:
                continue
            
            shortest[u] = w

            for n, c in graph[u]:
                if shortest[n] == -1:
                    heapq.heappush(minHeap, (w + c, n))


        return shortest