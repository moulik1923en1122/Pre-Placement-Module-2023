import collections 

class Solution:
    def firstUniqChar(self, s: str) -> int:
        chrs=defaultdict(lambda:0)
        for i in range(0,len(s)):
            chrs[''.join(s[i])]+=1
            
        for i in range(0,len(s)):
            if chrs[s[i]]==1:
                return i

      
        return -1