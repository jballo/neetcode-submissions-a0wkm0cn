class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # am i allowed to use other data structures?
        # is a certain space and/or time complexity preferred?

        # bottom up dp approach

        # cat
        # crabt

        matrix = []
        ROWS = len(text1)
        COLS = len(text2)

        for i in range(ROWS + 1):
            matrix.append(([0] * (COLS + 1)))

        #    c a t ""
        # c  3 2 1 0
        # r  2 2 1 0
        # a  2 2 1 0
        # b  1 1 1 0
        # t  1 1 1 0
        # "" 0 0 0 0
        
        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                if text1[r] == text2[c]:
                    matrix[r][c] = 1 + matrix[r+1][c+1]
                else:
                    matrix[r][c] = max(matrix[r+1][c], matrix[r][c+1], matrix[r+1][c+1])
        
        return matrix[0][0]

