from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        shortestPath = 1
        queue = deque()
        visited = set()
        queue.append((0,0))
        visited.add((0,0))
        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return shortestPath
                
                directions = [[-1,-1], [-1,0], [-1,1], [0,1], 
                              [1,1], [1,0], [1,-1], [0,-1]]

                for dr, dc in directions:
                    newR, newC = (r + dr), (c + dc)
                    if min(newR, newC) < 0 or newR >= ROWS or newC >= COLS or grid[newR][newC] == 1 or (newR, newC) in visited:
                        continue
                    
                    queue.append((newR, newC))
                    visited.add((newR, newC))

            shortestPath += 1

        return -1