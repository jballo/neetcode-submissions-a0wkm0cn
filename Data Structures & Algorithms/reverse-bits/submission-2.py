class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            lsb = n & 1
            newAmt = lsb << (31 - i)
            res |= newAmt
            n >>= 1

        return res