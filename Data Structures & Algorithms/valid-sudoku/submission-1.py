class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # unique set for row, col and box
        ROWS = len(board)
        COLS = len(board[0])
        C = {}
        box = {}
        for r in range(3):
            for c in range(3):
                box[(r,c)] = set()
        for c in range(COLS):
            C[c] = set()
        for r in range(ROWS):
            R = set()
            for c in range(COLS):
                if board[r][c] in R or board[r][c] in C[c] or board[r][c] in box[(r//3,c//3)]: 
                    print(board[r][c])
                    return False
                if board[r][c] != ".":
                    R.add(board[r][c])
                    C[c].add(board[r][c])
                    box[(r//3,c//3)].add(board[r][c])

                
            print(R)
        

        return True
                
