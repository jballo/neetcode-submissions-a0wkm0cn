class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0 # 1
        R = len(heights) -1 # 5
        maxWater = 0 # 36
        # [1,7,2,5,4,7,3,6]
        

        while L < R:
            water = (R - L) * min(heights[L], heights[R])
            maxWater = max(maxWater, water)
            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1

        return maxWater