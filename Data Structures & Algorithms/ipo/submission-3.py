import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        

        pricing = []
        for i in range(0, len(profits)):
            pricing.append((capital[i],profits[i]))

        
        heapq.heapify(pricing)

        maxProfits = []
        for _ in range(k):
            while pricing and w >= pricing[0][0]:
                heapq.heappush(maxProfits, -1 * heapq.heappop(pricing)[1])

            
            if maxProfits:
                curMaxProfit = -1 * heapq.heappop(maxProfits)
                w += curMaxProfit
        
        return w
