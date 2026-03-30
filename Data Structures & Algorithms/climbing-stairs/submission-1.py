class Solution:
    def climbStairs(self, n: int) -> int:
        return self.memo(n, {})

    def memo(self, step, cache):
        if step == 0:
            return 1
        elif step < 0:
            return 0
        elif step in cache:
            return cache[step]
        
        totSteps = self.memo(step - 1, cache) + self.memo(step - 2, cache)
        cache[step] = totSteps
        return totSteps