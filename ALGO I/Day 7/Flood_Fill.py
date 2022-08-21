class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        v = set()               
        color = image[sr][sc]
        row = len(image)
        col = len(image[0])
        def dfs(r,c):
            if (r,c) not in v:  
                v.add((r,c))
                image[r][c] = newColor
                
                if r+1 in range(row) and image[r+1][c] == color:
                    dfs(r+1,c)
                if r-1 in range(row) and image[r-1][c] == color:
                    dfs(r-1,c)
                if c-1 in range(col) and image[r][c-1] == color:
                    dfs(r,c-1)
                if c+1 in range(col) and image[r][c+1] == color:
                    dfs(r,c+1)
            else:
                return
       
        if image[sr][sc] == color and (sr,sc ) not in v:
            dfs(sr,sc)
                    
        return image
        
