import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        shortestTimes = {}

        for i in range(1, n + 1):
            shortestTimes[i] = -1

        graph = {}

        for ui, vi, ti in times:
            if ui not in graph:
                graph[ui] = []
            if vi not in graph:
                graph[vi] = []
            
            graph[ui].append((vi, ti))

        print(shortestTimes)

        minHeap = [(0, k)]


        while minHeap:
            ti, ui = heapq.heappop(minHeap)

            if shortestTimes[ui] != -1:
                continue
            
            shortestTimes[ui] = ti

            for n, c in graph[ui]:
                if shortestTimes[n] == -1:
                    heapq.heappush(minHeap, (ti + c, n))


        for cost in shortestTimes.values():
            if cost == -1:
                return -1

        return max(shortestTimes.values())

