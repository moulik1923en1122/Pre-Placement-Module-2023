class Solution:
    def isHappy(self, n: int) -> bool:
        hashSet=set()
        while True:
            n=self.sumSquareDigits(n)
            if n in hashSet:
                return  False
            else:
                if n==1:
                    return True 
                else:
                    hashSet.add(n)
    
    def sumSquareDigits(self,number):
        sum=0
        while number%10!=0 or number//10!=0:
            sum+=(number%10)**2
            number=number//10
        return sum