class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topLeftX, topLeftY = row1,col1
        bottomRightX, bottomRightY = row2, col2
        total = 0
        for i in range(topLeftX, bottomRightX+1):
            for j in range(topLeftY, bottomRightY+1):
                total += self.m[i][j]

        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


''' 3 0 1 4 2
    5 6 3 2 1
    1 2 0 1 5
    4 1 0 1 7
    1 0 3 0 5 '''