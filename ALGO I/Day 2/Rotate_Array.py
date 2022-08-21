class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[::-1]
        nums[0:k] = nums[0:k][::-1]
        nums[k:] = nums[k:][::-1]