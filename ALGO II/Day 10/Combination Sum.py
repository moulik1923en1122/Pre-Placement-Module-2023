class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.ans = []
        def dfs(candidates, num, path):
            
            
            
            if num < 0:
                return
            
            if num == 0:
                if sorted(path) not in self.ans:
                    self.ans.append(path)
                    return
            
            
            
            for i in range(len(candidates)):
                dfs(candidates[i:], num-candidates[i], path + [candidates[i]])
        
        dfs(candidates, target, [])
        
        return self.ans