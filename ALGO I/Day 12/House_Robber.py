class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:   
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]    ## Base case
        dp[1] = nums[1]    ## Base case
        for i in range(2, n):
            dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])   
        return max(dp[-1], dp[-2])