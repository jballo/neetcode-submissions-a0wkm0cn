class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # are there any space and/or time constraints?
        # am i allowed to use other data structures?

        # kadane's algorithm


        maxSum = nums[0]
        curSum = 0
        #                       
        # [2, -3, 4, -2, 2, 1, -1, 4]
        # maxSum = 8
        # curSum = 8

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum = n + curSum

            if curSum >= maxSum:
                maxSum = curSum
        
        return maxSum

