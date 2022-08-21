class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:    
        self.board = board
        self.word = word
        
      
        if len(word) == 0:
            return False
        
       
        all = []
        for x in range(len(board)):
            for y in range(len(board[0])):
                all.append(board[x][y])
        for c in word:
            if not c in all:
                return False
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
               
                if board[i][j] == word[0]:
                   
                    if (self.dfs(0, i, j, []) == True):
                        return True
        return False
    

    def dfs(self, cur, i, j, checked):
        
        if not (i<0 or j<0 or i>=len(self.board) or j>=len(self.board[0]) or 
                cur >= len(self.word) or self.board[i][j] != self.word[cur]):
            
            
            if not ((i,j) in checked):
                
                checked = checked[:cur]
                checked.append((i,j))

               
                if (cur == len(self.word)-1 and self.word[cur] == self.board[i][j]):
                    return True

               
                if (self.dfs(cur+1, i+1, j, checked) or
                    self.dfs(cur+1, i-1, j, checked) or
                    self.dfs(cur+1, i, j+1, checked) or
                    self.dfs(cur+1, i, j-1, checked)):
                    return True