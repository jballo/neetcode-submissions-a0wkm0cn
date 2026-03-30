
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # are we allowed to use other data structures?
        # are there any space and/or time constraints?
        
        # dfs w/ dp  approach
        # top down approach

        cache = []

        for i in range(m):
            row = [-1] * n
            cache.append(row)
        
        # cache = n * m of 0's

        def dfs(r, c):
            if r == m or c == n:
                return 0
            elif r == (m - 1) and c == (n - 1):
                return 1
            elif cache[r][c] > 0:
                return cache[r][c]
            
            pathCount = dfs(r + 1, c) + dfs(r, c + 1)
            cache[r][c] = pathCount
            return cache[r][c]

        return dfs(0,0)