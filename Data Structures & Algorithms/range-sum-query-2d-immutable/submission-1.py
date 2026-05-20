class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        # Obtain new matrix with prefix sums
        self.prefixArray = [[0] * (COLS + 1) for _ in range(ROWS+1)]
        for r in range(1, ROWS+1):
            for c in range(1, COLS+1):
                self.prefixArray[r][c] = self.prefixArray[r-1][c] + self.prefixArray[r][c-1] - self.prefixArray[r-1][c-1] + matrix[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topLeft = self.prefixArray[row1][col1]
        topRight = self.prefixArray[row1][col2+1]
        bottomLeft = self.prefixArray[row2+1][col1]
        bottomRight = self.prefixArray[row2+1][col2+1]

        return bottomRight - topRight - bottomLeft + topLeft 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

        