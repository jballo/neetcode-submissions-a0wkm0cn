class Solution:
    def countBits(self, n: int) -> List[int]:
        bitCountList = [0] * (n+1)
        memo = {}

        for i in range(n+1):
            bitCount = 0
            val = i
            while val:
                if val in memo:
                    bitCount += memo[val]
                    break
                val &= (val - 1)
                bitCount += 1
            bitCountList[i] = bitCount
            memo[i] = bitCount
        
        return bitCountList