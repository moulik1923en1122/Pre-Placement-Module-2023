class Solution(object):
    def wordBreak(self, s, wordDict):
       
        l=len(s)
        dp=[False]*(l+1)
        dp[0]=True
        for i in range(l):
            if dp[i]==True:
                for j in wordDict:
                    if s[i:i+len(j)]==j and i+len(j)<=l:
                        dp[i+len(j)]=True
        return dp[-1]