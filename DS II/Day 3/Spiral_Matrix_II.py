class Solution(object):
    def generateMatrix(self, n):
        output = []
        for i in range(n):
            output.append([])
            for j in range(n):
                output[i].append(0)
                
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        count = 1
        
        while left <= right and top <= bottom:
            
            for col in range(left, right + 1):
                output[top][col] = count
                count += 1
            top += 1
            
            for row in range(top, bottom + 1):
                output[row][right] = count
                count += 1
            right -= 1
            
            for col in range(right, left - 1, -1):
                output[bottom][col] = count
                count += 1
            bottom -= 1
            
            for row in range(bottom, top - 1, -1):
                output[row][left] = count
                count += 1
            left += 1
            
        return output