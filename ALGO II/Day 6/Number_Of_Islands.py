class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       
        ROWS, COLS = len(grid), len(grid[0])
       
        count = 0
        
       
        def dfs(r, c, grid):
            if(r < 0 or c < 0 or r==ROWS or c==COLS or grid[r][c] != "1"):
                return
            else:
             
                grid[r][c] = "*"
               
                dfs(r+1, c, grid)
                dfs(r, c+1, grid)
                dfs(r-1, c, grid)
                dfs(r, c-1, grid)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j, grid)
                    count += 1
        
        return count 