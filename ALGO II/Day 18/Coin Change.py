class Solution:
   
    def coinChange(self, coins: List[int], amount: int) -> int:
       
        dp = [amount+1] * (amount + 1)
        
        dp[0] = 0
       
        coins.sort()
        
        for i in range(1, amount+1, 1):
            for coin in coins:
                
                remainder = i - coin
                if(remainder >= 0):
                  
                    dp[i] = min(dp[i], dp[remainder] + 1)
                else:
                    break
        
        if(dp[amount] == (amount+1)):
            return -1
        return dp[amount]