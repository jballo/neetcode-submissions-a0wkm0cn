import heapq
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {}
        for j in range(n):
            graph[j] = []
        
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        
        minHeap = []
        visited = set()
        # print("graph: ", graph)
        for neigh, weigh in graph[0]:
            # print("neigh: ", neigh, " weigh: ", weigh)
            heapq.heappush(minHeap, (weigh, 0, neigh))

        visited.add(0)

        totalWeight = 0
        
        while minHeap:
            weight, src, dst = heapq.heappop(minHeap)
            if dst in visited:
                continue
            
            visited.add(dst)
            totalWeight += weight
            # print('dst: ', dst)
            for neigh, w in graph[dst]:
                if neigh not in visited:
                    heapq.heappush(minHeap, (w, dst, neigh))
        
        return totalWeight if len(visited) == n else -1


        

