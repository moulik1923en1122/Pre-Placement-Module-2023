class Solution(object):
    def generateParenthesis(self, n):
        
        def fn(i,j):
            
            if i==0:
                return [')'*j]
            if j<i:
                return []
            lis1=fn(i-1,j)
            lis2=fn(i,j-1)
            for l in range(len(lis1)):
                lis1[l]="("+lis1[l]
            for m in range(len(lis2)):
                lis2[m]=")"+lis2[m]
            return lis1+lis2
        return fn(n,n)