class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == "1":
                    islandCount += 1
                    self.dfs(grid, r, c, len(grid), len(grid[0]))

        return islandCount

    
    def dfs(self, grid, r, c, R, C):
        if min(r,c) < 0 or r >= R or c >= C or grid[r][c] == "0":
            return

        grid[r][c] = "0"
        self.dfs(grid, r-1, c, len(grid), len(grid[0]))
        self.dfs(grid, r+1, c, len(grid), len(grid[0]))
        self.dfs(grid, r, c-1, len(grid), len(grid[0]))
        self.dfs(grid, r, c+1, len(grid), len(grid[0]))