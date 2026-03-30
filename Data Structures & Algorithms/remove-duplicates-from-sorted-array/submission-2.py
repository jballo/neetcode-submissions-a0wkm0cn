class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0 # 4
        R = 1  # 5
        k = 1   # 4
        # [1,2,3,4,4]
        
        while R < len(nums):
            if nums[L] != nums[R]:
                nums[k] = nums[R]
                L = R
                k += 1
            R += 1
            
        return k