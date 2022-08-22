class Solution:
    def longestPalindrome(self, s: str) -> int:
        mapper = dict()
        for i in s:
            try:
                mapper[i]+=1
            except:
                mapper[i] = 1
        count = 0
        for i in mapper:
            if mapper[i]%2 != 0:
                count+=1
        if count > 0:
            return len(s)-count+1
        return len(s)