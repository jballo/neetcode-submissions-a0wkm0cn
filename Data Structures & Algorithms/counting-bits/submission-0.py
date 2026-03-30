class Solution:
    def countBits(self, n: int) -> List[int]:
        bitCountList = [0] * (n+1)

        for i in range(n+1):
            bitCount = 0
            val = i
            while val:
                val &= (val - 1)
                bitCount += 1
            bitCountList[i] = bitCount
        
        return bitCountList