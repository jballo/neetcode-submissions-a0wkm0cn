class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # do i have any space or time constraints?
        # am i allowed to use other data structures?
        # the 1s represent an obstacle?

        cache = []
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])

        for i in range(M):
            cache.append(([-1] * N))
        

        def dfs(r, c):
            if r >= M or c >= N:
                return 0
            elif obstacleGrid[r][c] == 1:
                return 0
            elif r == (M - 1) and c == (N - 1):
                return 1
            elif cache[r][c] > 0:
                return cache[r][c]


            cache[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[r][c]

        return dfs(0,0)

            


