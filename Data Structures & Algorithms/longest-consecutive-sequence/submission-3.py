class Union:
    def __init__(self, n):
        self.parents = [r for r in range(n)]
        self.ranks = [1] * n
        self.sizes = [1] * n
    
    def find(self, n):
        while n != self.parents[n]:
            self.parents[n] = self.parents[self.parents[n]]
            n = self.parents[n]

        return n

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False

        if self.parents[px] > self.parents[py]:
            self.parents[py] = px
            self.sizes[px] += self.sizes[py]
        elif self.parents[px] < self.parents[py]:
            self.parents[px] = py
            self.sizes[py] += self.sizes[px]
        else:
            self.parents[py] = px
            self.ranks[px] += 1
            self.sizes[px] += self.sizes[py]
    
        return True


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        valToIndices = {}
        if len(nums) == 0:
            return 0

        for i in range(0, len(nums)):
            if nums[i] not in valToIndices:
                valToIndices[nums[i]] = i
    
        connections = Union(len(nums))
        
        for val in valToIndices:
            if (val - 1) in valToIndices:
                connections.union(valToIndices[(val - 1)], valToIndices[val])

        return max(connections.sizes)


