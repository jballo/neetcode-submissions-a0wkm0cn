class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        subsets = []
        self.helper(0, nums, [], subsets)
        return subsets
    
    def helper(self, i, nums, subset, subsets):
        if i >= len(nums):
            subsets.append(subset.copy())
            return
        
        subset.append(nums[i])
        self.helper(i + 1, nums, subset, subsets)
        subset.pop()

        self.helper(i + 1, nums, subset, subsets)
