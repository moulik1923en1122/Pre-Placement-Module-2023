class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def help(nums):
            rob1 = rob2 = 0
            for item in nums:
                newRob = max(item+rob1, rob2)
                rob1 = rob2
                rob2 = newRob
            return rob2
        
        return max(nums[0], help(nums[1:]), help(nums[:-1]))