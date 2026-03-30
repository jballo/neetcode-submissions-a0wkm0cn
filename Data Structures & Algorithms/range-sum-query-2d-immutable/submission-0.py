class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.matrix = []
        for i in range(ROWS+1):
            self.matrix.append([0] * (COLS + 1))
        
        for i in range(ROWS):
            prefix = 0
            for j in range(COLS):
                prefix += matrix[i][j]
                self.matrix[i+1][j+1] = prefix + self.matrix[i][j+1]

        print(self.matrix)
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        maxSum = self.matrix[row2+1][col2+1]
        print(maxSum)
        left = self.matrix[row2 + 1][col1]
        top = self.matrix[row1][col2+1]
        intersect = self.matrix[row1][col1]
        return (maxSum - left - top + intersect)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)