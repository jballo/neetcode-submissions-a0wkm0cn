import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        highest = [-1] * n

        graph = {}
        for i in range(n + 1):
            graph[i] = []


        for i in range(len(edges)):
            edge = edges[i]
            a, b = edge[0], edge[1]
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))

        

        maxHeap = [(-1, start_node)]

        while maxHeap:
            p, n = heapq.heappop(maxHeap)
            print("p: ", p, " n: ", n)
            if highest[int(n)] != -1:
                continue
            
            highest[n] = -1 * p

            for n, np in graph[n]:
                if highest[n] != -1:
                    continue
                heapq.heappush(maxHeap, (p * np, n))

        
        return 0 if highest[end_node] == -1 else highest[end_node]