class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hm_row={str(i):set() for i in range(1,10)}
        hm_col={str(i):set() for i in range(1,10)}
        curbox=[set() for i in range(9)]
        for row in range(9):
            if row<3:
                curbox_ind=0
            elif row<6:
                curbox_ind=3
            else:
                curbox_ind=6        
            for col in range(9):
                # print(hm_row,hm_col,curbox,sep='\n')
                # print()
                if col in {3,6}:
                    curbox_ind+=1
                    # print(curbox_ind)
                
                if board[row][col]=='.':
                    continue
                if row not in hm_row[board[row][col]] :
                    hm_row[board[row][col]].add(row)
                else:
                    return False
                
                if col not in hm_col[board[row][col]] :
                    hm_col[board[row][col]].add(col)
                else:
                    return False
                
                if not board[row][col] in curbox[curbox_ind]:
                    curbox[curbox_ind].add(board[row][col])
                else:
                    return False
        return True 
        