class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        val = prices[0]
        profit = 0
        n = len(prices)
        for i in range(1,n):
            if prices[i]>val:
                curr_profit = prices[i]-val
                if curr_profit > profit:
                    profit = curr_profit
            else:
                val = prices[i]
        
        return profit
                