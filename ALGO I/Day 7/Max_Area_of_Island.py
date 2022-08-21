class Solution(object):
    def maxAreaOfIsland(self, grid):
        max_area =0
        visited = set()
        
        def computeArea(y,x):
            area = 0
            stack = [(y,x)]
            visited.add((y,x))
            
            while stack:
                i,j = stack.pop()
                area+=1
                
                if i<len(grid)-1 and grid[i+1][j]==1 and (i+1,j) not in visited:
                    stack.append((i+1,j))  
                    visited.add((i+1,j))
                if j<len(grid[i])-1 and grid[i][j+1]==1 and (i,j+1) not in visited:
                    stack.append((i,j+1))
                    visited.add((i,j+1))
                if i>0 and grid[i-1][j]==1 and (i-1,j) not in visited:
                    stack.append((i-1,j))
                    visited.add((i-1,j))
                if j>0 and grid[i][j-1]==1 and (i,j-1) not in visited:
                    stack.append((i,j-1))
                    visited.add((i,j-1))
            return area
         
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1 and grid[y][x] not in visited:
                    max_area = max(max_area,computeArea(y,x))
                    
        return max_area