class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
            res = []
    
            try:
                res.append(nums.index(target))
            except:
                return [-1,-1]
    
            nums = nums[::-1]
            n = len(nums)
            res.append(n - 1 - nums.index(target))
    
            return res
        