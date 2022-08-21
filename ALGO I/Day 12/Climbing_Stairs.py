class Solution(object):
    def climbStairs(self, n):
        arr = []
        arr.append(1)
        arr.append(2)
        for i in range(2, n):
            arr.append(arr[i-1] + arr[i-2])
        return arr[n-1]