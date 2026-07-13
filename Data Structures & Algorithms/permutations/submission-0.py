class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 0 [[2,3], [3, 2]]
        # 1 [[3]] res = [[2,3], [3,2]]
        # 2 [[]] res = [[3]]
        # 3
        def helper(i):
            if  i == len(nums):
                return [[]]

            returnedPerms = helper(i + 1)
            res = []

            for perm in returnedPerms:
                for j in range(0, len(perm) + 1):
                    copy = perm.copy()
                    copy.insert(j, nums[i])
                    res.append(copy)

            return res

        
        return helper(0)