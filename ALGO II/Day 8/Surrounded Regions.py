class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # start from the border to traverse (here, we choose BFS)
        m = len(board)
        n = len(board[0])

        from itertools import product
        borders = list(product(range(m), [0, n - 1])) \
                + list(product([0, m - 1], range(n)))
        
        dirs = [[0,1],[0,-1],[-1,0],[1,0]]
        
        queue = deque([])
        
        for x,y in borders:
            if board[x][y] == 'O':
                queue.append((x,y))
        
        while(queue):
            x, y = queue.popleft()
            board[x][y] = 'E'
            for mov_x, mov_y in dirs:
                if (x + mov_x >=0) and (x + mov_x <= m - 1) and  (y + mov_y >=0) and (y + mov_y <= n - 1) and board[x + mov_x][y + mov_y] == 'O':
                    queue.append((x + mov_x, y + mov_y))
        
        for x in range(m):
            for y in range(n):
                if board[x][y] == 'E':
                    board[x][y] = 'O'
                elif board[x][y] == 'O':
                    board[x][y] = 'X'