class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        i,j = 0,0
        result = []
        
        while i<len(firstList) and j<len(secondList):
            si,ei = firstList[i]
            sj,ej = secondList[j]
            
            if si<=ej and sj<=ei:
                result.append([max(si,sj),min(ei,ej)])
                
            if ei>ej:
                j+=1
            elif ej>ei:
                i+=1
            else:
                i+=1
                j+=1
        
        return result