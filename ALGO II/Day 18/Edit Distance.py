class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        
        def dp(i, j, memo={}):
            
            key = f"{i},{j}"
            if key in memo:
                return memo[key]
            
            
            if i == n or j == m:
                len1, len2 = len(word1[i:]), len(word2[j:])
                return max(len1, len2)
            
            if word1[i] == word2[j]:
                memo[key]=dp(i+1, j+1)
                return memo[key]
            else:
                memo[key] = min(dp(i+1, j), dp(i, j+1), dp(i+1, j+1)) + 1
                return memo[key]
                
        return dp(0, 0)