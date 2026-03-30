#.      3
#    2.   1
# 1    0. 0  -1
# 0 -1

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        elif n == 0:
            return 1

        leftSum = self.climbStairs(n - 1)
        rightSum = self.climbStairs(n - 2)
        return leftSum + rightSum