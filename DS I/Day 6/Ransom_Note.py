class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine)<len(ransomNote):
            return False
        for i in range(len(ransomNote)):
            check=False
            for j in range(len(magazine)):
                if magazine[j]==ransomNote[i]:
                    check=True 
                    magazine=magazine[:j]+magazine[j+1:]
                    break
            if check==False:
                return False 
        return True