from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        shortestPath = 0
        queue = deque()
        visited = set()
        queue.append((0,0))
        visited.add((0,0))
        ROWS, COLS = len(grid), len(grid[0])

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                # if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == 1 OR ((r,c))
                if r == (ROWS - 1) and c == (COLS - 1):
                    return shortestPath
                
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                for dr, dc in directions:
                    if min((r + dr), (c + dc)) < 0 or (r + dr) >= ROWS or (c + dc) >= COLS or grid[r + dr][c + dc] == 1 or ((r + dr), (c + dc)) in visited:
                        continue
                    queue.append(((r + dr), (c + dc)))
                    visited.add(((r + dr), (c + dc)))

            
            shortestPath += 1

        return -1

                
            