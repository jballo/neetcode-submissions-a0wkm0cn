class Solution:
    def reverseBits(self, n: int) -> int:
        #am i able to create another number, or does it have to mutate n?

        newNum = 0
        for i in range(1, 33):
            if n & 1 == 1:
                added = (2 ** (32 - i))
                print(added)
                newNum += added
            n = n >> 1

        return newNum
