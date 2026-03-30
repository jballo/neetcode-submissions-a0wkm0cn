class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # positive numbers
        # contiguous
        # no subarray return 0
        minLen = len(nums) + 1 # 1
        L = 0 # 1
        curSum = 0 # 5
        # target = 5, nums = [3]
        # i = 

        for R in range(len(nums)):
            curSum += nums[R]
            while curSum >= target:
                minLen = min(minLen, (R - L + 1))
                curSum -= nums[L]
                L += 1
        
        return minLen if minLen != (len(nums) + 1) else 0

