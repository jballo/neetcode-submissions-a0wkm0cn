import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        shortest = []
        for _ in range(len(grid)):
            shortest.append([-1] * len(grid[0]))

        # 0 -> weight
        # (weight, row, column)
        minHeap = [(grid[0][0], 0, 0)]

        while minHeap:
            w, r, c = heapq.heappop(minHeap)
            if shortest[r][c] != -1:
                continue
            # r, c
            shortest[r][c] = w
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                if (r + dr) < 0 or (c + dc) < 0 or (r + dr) >= ROWS or (c + dc) >= COLS or shortest[r + dr][c + dc] != -1:
                    continue
                
                heapq.heappush(minHeap, (max(w, grid[r + dr][c + dc]), r + dr, c + dc))

        for i in range(len(shortest)):
            print(shortest[i])
            
        
        return shortest[ROWS - 1][COLS - 1]