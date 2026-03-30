class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n
        # i = 3, n = 4
        # [1,4,1,2]
        # [1, 4, 1, 2, 1, 4, 1, 2]

        for i in range(0, len(nums)):
            ans[i] = nums[i]
            ans[i+n] = nums[i]

        return ans