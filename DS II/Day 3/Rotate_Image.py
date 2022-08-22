class Solution(object):
    def rotate(self, matrix):
        for row in range(len(matrix)):
            for col in range(row+1):
                if col != row:
                    matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        for row in range(len(matrix)):
            matrix[row] = matrix[row][::-1]
        return matrix