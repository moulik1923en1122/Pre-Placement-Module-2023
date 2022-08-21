class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans=[]
        def backtrack(i,temp):
            if i==len(s):
                ans.append(temp)
                return
            if (ord(s[i])<=90 and ord(s[i])>=65):
                backtrack(i+1,temp+s[i].lower()) 
                backtrack(i+1,temp+s[i]) 
            elif (ord(s[i])<=122 and ord(s[i])>=97):
                backtrack(i+1,temp+s[i].upper()) 
                backtrack(i+1,temp+s[i]) 
            else:
                backtrack(i+1,temp+s[i])
        backtrack(0,"")
        return ans