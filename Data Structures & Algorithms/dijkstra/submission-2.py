import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        rep = {}

        for u, v, w in edges:
            if u not in rep:
                rep[u] = []
            if v not in rep:
                rep[v] = []

            rep[u].append((v, w))

        shortest = {}
        # for u, v, w in edges:
        #     if u not in shortest:
        #         shortest[u] = -1
        #     if v not in shortest:
        #         shortest[v] = -1
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        # shortest[src] = 0
        minHeap = [(0, src)]
        # print(rep)

        while minHeap:
            w, u = heapq.heappop(minHeap)
            # print("u: ", u, ", v: ", w)
            if shortest[u] != -1:
                continue
            
            shortest[u] = w
            
            for n, c in rep[u]:
                if shortest[n] == -1:
                    heapq.heappush(minHeap, (c + w, n))

        return shortest
            

        
        

