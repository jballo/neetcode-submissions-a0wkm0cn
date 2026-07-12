class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []

        def helper(i, curSum, combo):
            if curSum == target:
                combos.append(combo.copy())

            if curSum > target or i >= len(nums):
                return
                
            for j in range(i, len(nums)):
                combo.append(nums[j])
                helper(j, curSum + nums[j], combo)
                combo.pop()

        helper(0, 0, [])
        return combos