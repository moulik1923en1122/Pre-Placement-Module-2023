class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s, ind, min_len = 0, 0, float('inf')
        for i in range(len(nums)):
            s += nums[i]
            while s >= target:
                min_len = min(min_len, i - ind + 1)
                s -= nums[ind]
                ind += 1
        return min_len if min_len != float('inf') else 0