class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        out = [False]

        def DFS(r,c,v,t):
            # print(v)
            if len(v) > len(word):
                return
            if (r,c) in t:
                return

            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return

            v.append(board[r][c])
            t.add((r,c))

            if "".join(v) == word:
                out[0] = True
                return
            if r-1 >= 0:
                DFS(r-1, c, v, t)
            if r+1 < ROWS:
                DFS(r+1, c, v, t)
            if c-1 >= 0:
                DFS(r, c-1, v, t)
            if c+1 < COLS:
                DFS(r, c+1, v, t)
                
            v.pop()
            t.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    DFS(r,c,[],set())
        
        return out[0]
        
            
                