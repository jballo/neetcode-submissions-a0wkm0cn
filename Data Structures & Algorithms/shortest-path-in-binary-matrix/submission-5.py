from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        path = 1

        if grid[0][0] == 1:
            return -1

        queue = deque()
        queue.append((0,0))
        ROWS, COLS = len(grid), len(grid[0])

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return path
                
                grid[r][c] = 1
                directions = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]

                for dr, dc in directions:
                    nr, nc = (dr + r), (dc + c)
                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 1:
                        continue

                    queue.append((nr,nc))

            path += 1

        return -1