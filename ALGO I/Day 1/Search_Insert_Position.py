class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            l=0
            while l<len(nums):
                if target>nums[l]:
                    l=l+1
                else:
                    return l
            return l