class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        res = 0
        i, j, diff = 0, 1, nums[1]-nums[0]
        while j < len(nums):
            newDiff = nums[j]-nums[j-1]
            if newDiff != diff:
                res += (j-i-1)*(j-i-2)//2
                i, diff = j-1, newDiff
            j += 1
        res += (j-i-1)*(j-i-2)//2
        return res