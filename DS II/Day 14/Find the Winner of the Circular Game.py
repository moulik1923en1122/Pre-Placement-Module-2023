class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def solve(arr,start,k):
            if len(arr) == 1:
                return arr[0]
            idx = (start+k-1)%len(arr)
            arr.pop(idx)
            return solve(arr,idx,k)
        arr = [i for i in range(1,n+1)]
        return solve(arr,0,k)