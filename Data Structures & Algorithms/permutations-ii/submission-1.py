class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # create a frequency dictionary
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 0
            frequency[num] += 1

        # create a recursive helper function()
        #  if len()
        print(frequency)

        perms = []
        perm = []

        def dfs():
            if len(perm) == len(nums):
                perms.append(perm.copy())
            
            for key in frequency:
                if frequency[key] > 0:
                    perm.append(key)
                    frequency[key] -= 1
                    dfs()
                    perm.pop()
                    frequency[key] += 1

        dfs()

        return perms