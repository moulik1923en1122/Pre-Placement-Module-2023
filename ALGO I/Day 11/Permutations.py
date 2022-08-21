class Solution(object):
    def permute(self, nums):
        
        res = []
        def dfs(path, num): 
            if not num:
                res.append(path)   
                return
            for i in range(len(num)):
                dfs(path + [num[i]], num[:i] + num[i + 1:]) 
               
        
        dfs([], nums)
        return res