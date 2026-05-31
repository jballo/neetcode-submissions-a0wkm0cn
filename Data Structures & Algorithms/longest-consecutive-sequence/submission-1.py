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
        
        if self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
            self.sizes[px] += self.sizes[py]
        elif self.ranks[px] < self.ranks[py]:
            self.parents[px] = py
            self.sizes[py] += self.sizes[px]
        else:
            self.parents[py] = px
            self.ranks[px] += 1
            self.sizes[px] += self.sizes[py]
        
        return True

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        connections = Union(len(nums))
        indexPairing = {}

        for i in range(len(nums)):
            if nums[i] not in indexPairing:
                indexPairing[nums[i]] = i
        

        for key in indexPairing:
            # if key - 1 in indexPairing:
            #     connections.union(indexPairing[key], indexPairing[key - 1])
            if key + 1 in indexPairing:
                connections.union(indexPairing[key], indexPairing[key + 1])

        return max(connections.sizes)


