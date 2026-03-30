class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # bottom up dp approach

        matrix = []
        # aat
        # crabt

        #     a a t ""
        # c   0 0 0 0
        # r   0 0 0 0
        # a   0 0 0 0
        # b   0 0 0 0
        # t   0 0 0 0
        # ""  0 0 0 0


        ROWS = len(text1)
        COLS = len(text2)

        for r in range(ROWS+1):
            matrix.append(([0] * (COLS + 1)))
        
        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                if text1[r] == text2[c]:
                    matrix[r][c] = 1 + matrix[r+1][c+1]
                else:
                    matrix[r][c] = max(matrix[r+1][c], matrix[r][c+1])

        return matrix[0][0]