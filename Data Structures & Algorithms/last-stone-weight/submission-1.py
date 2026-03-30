class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(0, len(stones)):
            stones[i] = stones[i] * -1

        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            # X   Y
            # -9, -8
            if x < y:
                heapq.heappush(stones, x - y)
            
        heapq.heappush(stones, 0)
        return -stones[0]

            
