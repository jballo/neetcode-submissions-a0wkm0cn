from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
    
        shortestPath = 0
        queue = deque()
        queue.append((0,0))

        ROWS, COLS = len(grid), len(grid[0])

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return shortestPath
                grid[r][c] = 1
                directions = [[-1,0], [0,1], [1,0], [0, -1]]

                for dr, dc in directions:
                    nR, nC = (r + dr), (c + dc)
                    if min(nR, nC) < 0 or nR == ROWS or nC == COLS or grid[nR][nC] == 1:
                        continue

                    queue.append((nR, nC))

            shortestPath += 1

        return -1
