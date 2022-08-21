class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        lis=[]
        for i, ch in enumerate(s):
            if not ch in lis:
                lis.append(ch)                
            else:
                longest=longest if longest>len(lis) else len(lis)
                lis=lis[lis.index(ch)+1:]
                lis.append(ch)
        longest=longest if longest>len(lis) else len(lis)
        return longest
        