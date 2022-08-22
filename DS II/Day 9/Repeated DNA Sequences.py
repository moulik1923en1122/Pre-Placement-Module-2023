class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic = {}  # dictionary to store frequency of sequences
        i = 0
        j = 9
        while j < len(s):
            if s[i:j+1] in dic:
                dic[s[i:j+1]] += 1
            else:
                dic[s[i:j+1]] = 1
            i += 1
            j += 1
        res = []
        for k in dic:
            if dic[k] > 1:
                res.append(k)
        return res