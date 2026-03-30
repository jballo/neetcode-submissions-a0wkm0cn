class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax = nums[0]
        globalMin = nums[0]
        curMax = 0
        curMin = 0
        total = 0

        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            total += n
            globalMax = max(curMax, globalMax)
            globalMin = min(curMin, globalMin)

        if globalMax < 0:
            return globalMax
        
        circularMaxSum = total - globalMin

        if circularMaxSum > globalMax:
            return circularMaxSum

        return globalMax
