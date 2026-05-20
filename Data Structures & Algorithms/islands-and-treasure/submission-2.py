class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # from treasure chest do DFS and update gridPositions if smaller dist
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c, 0))
        
        # do BFS
        while queue:
            length = len(queue)
            for i in range(length):
                r,c,d = queue.popleft()
                grid[r][c] = min(grid[r][c], d)
                if r-1 >=0 and grid[r-1][c] == 2147483647:
                    queue.append((r-1,c,d+1)) 
                if c-1 >=0 and grid[r][c-1] == 2147483647:
                    queue.append((r,c-1,d+1)) 
                if r+1 < ROWS and grid[r+1][c] == 2147483647:
                    queue.append((r+1,c,d+1))
                if c+1 < COLS and grid[r][c+1] == 2147483647:
                    queue.append((r,c+1,d+1))
            

        

                 




                
                    

        