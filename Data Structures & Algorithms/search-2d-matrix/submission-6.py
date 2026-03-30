class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bottom = ROWS - 1

        while top <= bottom:
            m = (top + bottom) // 2

            if target < matrix[m][0]:
                bottom = m - 1
            elif target > matrix[m][-1]:
                top = m + 1
            else:
                break
        
        if top > bottom:
            return False

        left = 0
        right = COLS - 1
        row = (top + bottom) // 2

        while left <= right:
            col = (left + right) // 2

            if target > matrix[row][col]:
                left = col + 1
            elif target < matrix[row][col]:
                right = col - 1
            else:
                return True

        return False
