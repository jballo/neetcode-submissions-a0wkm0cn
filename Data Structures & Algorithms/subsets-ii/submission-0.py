class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        subsets = []


        def helper(i, subset):
            if i >= len(nums):
                subsets.append(subset.copy())
                return

            subset.append(sortedNums[i])
            helper(i + 1, subset)
            subset.pop()
            while i + 1 < len(nums) and sortedNums[i + 1] == sortedNums[i]:
                i += 1

            helper(i + 1, subset)
            return

        helper(0, [])

        return subsets