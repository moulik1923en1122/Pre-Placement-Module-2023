class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, j, n = 0, 0, len(nums)
        while j < n and nums[j] != 0: j += 1
        while True:
            while i < n and nums[i] != 0: i += 1
            while j < n and nums[j] == 0: j += 1
            if i >= n or j >= n or i >= j: return
            nums[i], nums[j] = nums[j], nums[i]