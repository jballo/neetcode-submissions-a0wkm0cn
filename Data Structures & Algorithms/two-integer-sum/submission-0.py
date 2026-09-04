class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in visited:
                return [visited[difference], i]
            visited[nums[i]] = i