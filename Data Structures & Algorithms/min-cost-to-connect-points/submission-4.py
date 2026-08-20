import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {}


        for i in range(len(points)):
            oX = points[i][0]
            oY = points[i][1]
            graph[(oX, oY)] = []
            for j in range(len(points)):
                if j == i:
                    continue
                nX = points[j][0]
                nY = points[j][1]
                distance = abs(oX - nX) + abs(oY - nY)

                graph[(oX, oY)].append((nX, nY, distance))
        

        minHeap = [(0, points[0][0], points[0][1])]
        visited = set()
        minCost = 0

        while minHeap and len(visited) < len(points):
            dist, x, y = heapq.heappop(minHeap)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            minCost += dist

            for nX, nY, nDist in graph[(x, y)]:
                if (nX, nY) not in visited:
                    heapq.heappush(minHeap, (nDist, nX, nY))
        
        return minCost


