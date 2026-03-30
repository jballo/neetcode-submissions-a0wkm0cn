import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceRep = []
        for point in points:
            distance = -math.sqrt(((point[0])**2) + ((point[1])**2))
            distanceRep.append((distance, point))

        
        heapq.heapify(distanceRep)
        
        while len(distanceRep) > k:
            heapq.heappop(distanceRep)
        
        closestPoints = []

        for point in distanceRep:
            closestPoints.append(point[1])

        return closestPoints
        