class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        discoveredRows = []
        discoveredCols = []
        discoveredSeg = []
        for _ in range(9):
            discoveredRows.append(set())
            discoveredCols.append(set())

        for r in range(3):
            row = []
            for c in range(3):
                row.append(set())
            discoveredSeg.append(row)

        # 0, 1, 2, 3, 4, 5, 6, 7, 8
        # 0 // 3 = 0
        #  2 // 3 = 0
        #  
        
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in discoveredRows[r]:
                    return False
                elif val in discoveredCols[c]:
                    return False
                elif val in discoveredSeg[r // 3][c // 3]:
                    return False
                
                discoveredRows[r].add(val)
                discoveredCols[c].add(val)
                discoveredSeg[r // 3][c // 3].add(val)
                

        return True
