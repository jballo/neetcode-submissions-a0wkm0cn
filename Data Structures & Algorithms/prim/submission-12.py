import heapq
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {}
        for j in range(n):
            graph[j] = []
        
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        
        minHeap = [(0, 0)]
        visited = set()
        totalWeight = 0
        
        while minHeap and len(visited) < n:
            weight, src = heapq.heappop(minHeap)
            if src in visited:
                continue
            
            visited.add(src)
            totalWeight += weight
            for neigh, w in graph[src]:
                if neigh not in visited:
                    heapq.heappush(minHeap, (w, neigh))
        
        return totalWeight if len(visited) == n else -1


        

