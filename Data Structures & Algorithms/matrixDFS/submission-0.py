class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        return self.dfs(grid, 0, 0, len(grid), len(grid[0]), set())
    
    def dfs(self, grid, r, c, R, C, visited):
        if min(r,c) < 0 or r >= R or c >= C or (r,c) in visited or grid[r][c] == 1:
            return 0
        elif r == (R - 1) and c == (C - 1):
            return 1

        
        pathCount = 0
        visited.add((r,c))
        pathCount += self.dfs(grid, r - 1, c, R, C, visited)
        pathCount += self.dfs(grid, r + 1, c, R, C, visited)
        pathCount += self.dfs(grid, r, c - 1, R, C, visited)
        pathCount += self.dfs(grid, r, c + 1, R, C, visited)
        
        visited.remove((r,c))
        return pathCount