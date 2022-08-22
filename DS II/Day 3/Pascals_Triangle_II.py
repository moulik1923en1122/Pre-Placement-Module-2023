class Solution(object):
    def getRow(self, rowIndex):
        a = rowIndex
        rows = [[1]]
        for r in range(1, rowIndex+1):
            rows.append([1] * (r+1))
            for c in range(1, r):
                rows[r][c] = rows[r-1][c] + rows[r-1][c-1]
        return rows[a]