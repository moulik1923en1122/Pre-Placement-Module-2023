class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        
        totaloranges = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                if grid[r][c] != 0:
                    totaloranges += 1
        
        time = 0
        while q:
            r, c, time = q.popleft()
            
            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                x = r + dr
                y = c + dc
                
                if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] != 1:
                    continue
                    
                q.append((x, y, time + 1))
                grid[x][y] = 2
                
        return time if totaloranges == sum(sum(grid, [])) // 2 else -1