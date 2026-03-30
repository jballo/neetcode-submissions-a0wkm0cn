class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [0] * n

        for r in range(m - 1, -1, -1):
            newRow = [1] * n
            for c in range(n - 2, -1, -1):
                newRow[c] = newRow[c + 1] + row[c]
            row = newRow

        return row[0]
