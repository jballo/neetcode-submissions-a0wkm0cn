import heapq
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {}

        for i in range(n):
            graph[i] = []

        
        for src, dst, weight in edges:
            graph[src].append((dst, weight))
            graph[dst].append((src, weight))
        
        visited = set()
        minHeap = []
        visited.add(0)
        for neigh, w in graph[0]:
            heapq.heappush(minHeap, (w, 0, neigh))

        totWeight = 0
        while minHeap:
            weight, src, dst = heapq.heappop(minHeap)

            if dst in visited:
                continue

            visited.add(dst)
            totWeight += weight

            for neigh, w in graph[dst]:
                if neigh not in visited:
                    heapq.heappush(minHeap, (w, dst, neigh))


        return totWeight if len(visited) == n else -1
