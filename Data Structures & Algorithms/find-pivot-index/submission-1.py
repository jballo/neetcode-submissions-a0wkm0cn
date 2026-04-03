class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total += num

        # [1,7,3,6,5,6]
        #  total = 28
        # 11
        prefix = 0 # 8

        for i in range(len(nums)):
            if prefix == (total - prefix - nums[i]):
                return i
            prefix += nums[i]

        
        return -1