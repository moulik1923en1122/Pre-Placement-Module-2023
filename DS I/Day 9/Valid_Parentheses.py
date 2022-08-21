class Solution:
    def isValid(self, s: str) -> bool:
        m = {'(':')', '{':'}','[':']'}
        stack = []
        
        for j in s:
            if j in m:
                stack.append(j)
            elif len(stack) == 0 or m[stack.pop()] != j:
                return False
        
        return len(stack) == 0