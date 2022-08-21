from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        finList=[]
        result=[]
        if len(digits)==0:
            return result
        mystr=''
        for i in digits:
            mystr=d[int(i)]
           
            chunk=len(mystr)
            a=[ mystr[i:i+1] for i in range(0,chunk , 1) ]
            finList.append(a)
        
     
        for element in itertools.product(*finList):
            st = ''.join(map(str, element))
         
            result.append(st)

        
        return(result)