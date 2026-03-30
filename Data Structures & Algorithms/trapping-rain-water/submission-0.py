class Solution:
    def trap(self, height: List[int]) -> int:
        L, R, lMax, rMax = 1, (len(height) - 2), height[0], height[len(height) - 1]
        trappedWater = 0


        while L <= R:
            if lMax <= rMax:
                maxHeight = lMax - height[L]
                maxHeight = maxHeight if maxHeight > 0 else 0
                trappedWater += maxHeight
                lMax = height[L] if height[L] >= lMax else lMax
                L += 1
            else:
                maxHeight = rMax - height[R]
                maxHeight = maxHeight if maxHeight > 0 else 0
                trappedWater += maxHeight
                rMax = height[R] if height[R] >= rMax else rMax
                R -= 1

        return trappedWater