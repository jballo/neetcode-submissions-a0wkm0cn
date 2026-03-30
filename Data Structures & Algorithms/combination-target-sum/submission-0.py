class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sumList = []
        combination = []

        self.dfs(sumList, combination, nums, 0, target, 0)
        return sumList

    def dfs(self, sumList, combination, nums, total, target, i):
        if i >= len(nums) or total > target:
            return
        elif total == target:
            sumList.append(combination.copy())
            return
        
        combination.append(nums[i])
        self.dfs(sumList, combination, nums, total + nums[i], target, i)
        combination.pop()
        self.dfs(sumList, combination, nums, total, target, i + 1)
        