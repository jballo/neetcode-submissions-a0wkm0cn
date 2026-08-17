import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        shortest = []
        ROWS = len(grid)
        COLS = len(grid[0])
        for _ in range(ROWS):
            shortest.append([-1] * COLS)

        
        minHeap = [(grid[0][0], 0, 0)]

        while minHeap:
            w, r, c = heapq.heappop(minHeap)
            if shortest[r][c] != -1:
                continue

            shortest[r][c] = w

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or shortest[nr][nc] != -1:
                    continue

                heapq.heappush(minHeap, (max(w, grid[nr][nc]), nr, nc))
            
        return shortest[ROWS - 1][COLS - 1]