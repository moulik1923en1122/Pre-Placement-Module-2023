class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visit = deque()
        self.h = len(mat)
        self.l = len(mat[0])
        
#         Empty mat
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1:
                    mat[r][c] = math.inf
                else:
                    visit.append((r, c))

        while visit:
            r, c = visit.popleft()
            small = mat[r][c]+1
            for nr, nc in self.getNeighbors(r,c):
                if mat[nr][nc] > small:
                    mat[nr][nc] = small
                    visit.append((nr, nc))
        return mat
                    
    def getNeighbors(self, r , c):
        ret = []
        if r > 0:
            ret += [(r-1,c)]
        if c > 0:
            ret += [(r,c-1)]
        if r < self.h-1:
            ret += [(r+1,c)]
        if c < self.l-1:
            ret += [(r,c+1)]
        return ret