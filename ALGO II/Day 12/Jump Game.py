class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach, n = 0, len(nums) 
        for i, elem in enumerate(nums): 
            if max_reach < i: 
                return False
            if max_reach >= n - 1:
                return True
            max_reach = max(max_reach, i + elem)