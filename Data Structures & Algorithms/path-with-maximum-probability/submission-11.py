import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        highestProbs = [-1] * n

        graph = {}
        for src in range(n):
            graph[src] = []

        # build graph
        for i in range(len(edges)):
            src, dest = edges[i][0], edges[i][1]
            graph[src].append((dest, succProb[i]))
            graph[dest].append((src, succProb[i]))

        
        maxHeap = [(-1, start_node)]

        while maxHeap:
            p, n = heapq.heappop(maxHeap)
            if n == end_node:
                return -p
            if highestProbs[n] != -1:
                continue

            highestProbs[n] = p

            for neigh, nextp in graph[n]:
                if highestProbs[neigh] != -1:
                    continue
                
                heapq.heappush(maxHeap, (p * nextp, neigh))

        return 0 if highestProbs[end_node] == -1 else -highestProbs[end_node]

