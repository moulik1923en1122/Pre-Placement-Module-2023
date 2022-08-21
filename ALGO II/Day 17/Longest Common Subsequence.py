class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def lcs(index1, index2):
            if index1 < 0 or index2 < 0:
                return 0
            if text1[index1] == text2[index2]:
                if(index1-1, index2-1) in dp:
                    return 1+dp[(index1-1, index2-1)]
                else:
                    return 1+ lcs(index1-1, index2-1)
            else:
                if (index1-1, index2) in dp:
                    moveIndex1by1 = dp[(index1-1, index2)]
                else:
                    moveIndex1by1 = lcs(index1-1, index2)
                if (index1, index2-1) in dp:
                    moveIndex2By1 = dp[(index1, index2-1)]
                else:
                    moveIndex2By1 = lcs(index1, index2-1)
                dp[(index1, index2)] = max(moveIndex2By1, moveIndex1by1)
                return dp[(index1, index2)]
    
        return lcs(len(text1)-1, len(text2)-1)