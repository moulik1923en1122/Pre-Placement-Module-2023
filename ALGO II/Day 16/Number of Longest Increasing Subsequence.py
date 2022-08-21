class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        freq = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and 1 + dp[j] >= dp[i]:
                    if dp[i] == 1 + dp[j]:
                        freq[i] += freq[j]
                    else:
                        freq[i] = freq[j]
                    dp[i] = 1 + dp[j]

        maximal = max(dp)
        res = 0
        for idx, num in enumerate(dp):
            if num == maximal:
                res += freq[idx]
        
        return res