class Solution(object):
    def sortedSquares(self, nums):
     
        low  = 0
        high = len(nums) - 1
        result = [None for i in range(len(nums))]
        
        for i in reversed(range(len(nums))):
            if abs(nums[low]) > abs(nums[high]):
                result[i] = nums[low]**2
                low = low + 1
            else:
                result[i] = nums[high]**2
                high = high - 1
        return result