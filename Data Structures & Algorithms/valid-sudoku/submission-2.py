class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dR = []
        dC = []
        dS = []

        for i in range(9):
            dR.append(set())
            dC.append(set())

        for r in range(3):
            row = []
            for c in range(3):
                row.append(set())
            dS.append(row)

        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                if val in dR[r]:
                    return False
                elif val in dC[c]:
                    return False
                elif val in dS[r // 3][c // 3]:
                    return False

                dR[r].add(val)
                dC[c].add(val)
                dS[r // 3][c // 3].add(val)

        return True

        