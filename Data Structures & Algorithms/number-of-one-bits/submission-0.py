class Solution:
    def hammingWeight(self, n: int) -> int:
    
        oneBitCount = 0

        while n > 0:
            if n & 1 == 1:
                oneBitCount += 1
            n = n >> 1
        
        return oneBitCount
