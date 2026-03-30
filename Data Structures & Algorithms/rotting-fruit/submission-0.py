from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        freshCnt = 0
        rotten = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshCnt +=1
                elif grid[r][c] == 2:
                    rotten.append((r,c))
        
        minutes = 0

        while freshCnt > 0 and rotten:
            for i in range(len(rotten)):
                r, c = rotten.popleft()

                directions = [[-1,0], [1,0], [0,-1], [0,1]]

                for dr, dc in directions:
                    nr, nc = (r + dr), (c + dc)
                    if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue
                    freshCnt -= 1
                    grid[nr][nc] = 2
                    rotten.append((nr,nc))

            minutes += 1

        
        if freshCnt > 0:
            return -1

        return minutes
        