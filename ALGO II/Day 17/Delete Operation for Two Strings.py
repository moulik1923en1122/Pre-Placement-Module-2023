from functools import cache
class Solution:
    @cache
   
    def minDistance(self, word1: str, word2: str) -> int:
        for ix, (l, k) in enumerate(zip(word1, word2)):
            if l != k:
                del1 = 1 + self.minDistance(word1[ix+1:], word2[ix:])
                del2 = 1 + self.minDistance(word1[ix:], word2[ix+1:])
                return min(del1, del2)
		
		
        if len(word1) != len(word2):
            return abs(len(word1)-len(word2))

        return 0  