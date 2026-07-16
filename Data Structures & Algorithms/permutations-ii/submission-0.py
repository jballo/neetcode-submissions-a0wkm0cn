class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for i in range(len(nums)):
            cur = []
            for perm in perms:
                for j in range(len(perm) + 1):
                    pCopy = perm.copy()
                    pCopy.insert(j, nums[i])
                    cur.append(pCopy)
            perms = cur

        
        permsVisited = set()
        uniquePerms = []

        for perm in perms:
            key = tuple(perm)
            if key not in permsVisited:
                permsVisited.add(key)
                uniquePerms.append(perm)
        
        return uniquePerms