class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = [0]
        visited = set()
        maxArea = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def DFS(r,c):
            print(area[0])
            if r >= 0 and r < ROWS and c >=0 and c < COLS and (r,c) not in visited:
                if grid[r][c]== 1:
                    visited.add((r,c))
                    area[0] += 1
                    DFS(r-1,c)
                    DFS(r+1,c)
                    DFS(r, c-1)
                    DFS(r, c+1)

                else:
                    return False
            
            else:
                return False
    

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    DFS(r,c)
                    maxArea = max(maxArea, area[0])
                    area[0] = 0
        return maxArea
                    
