class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxAreaSurface = 0
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                area = self.dfs(grid, r, c, R, C)
                if area > maxAreaSurface:
                    maxAreaSurface = area

        return maxAreaSurface
        

    def dfs(self, grid, r, c, R, C):
        if min(r, c) < 0 or r >= R or c >= C or grid[r][c] == 0:
            return 0

        area = 1
        grid[r][c] = 0
        area += self.dfs(grid, r-1, c, R, C)
        area += self.dfs(grid, r+1, c, R, C)
        area += self.dfs(grid, r, c-1, R, C)
        area += self.dfs(grid, r, c+1, R, C)

        return area
        