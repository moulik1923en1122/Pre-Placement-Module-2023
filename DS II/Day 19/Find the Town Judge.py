class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        arr = []
        d = {}
        
        for i in range(1, n+1):
            arr.append(i)
            d[i] = []
            
        for i in trust:
            d[i[1]].append(i[0])
            if i[0] in arr:
                arr.remove(i[0])
        
        if len(arr)!=1:
            return -1
        
        for key, value in d.items():
            if key==arr[0] and len(value)==n-1:
                return key
        
        return -1