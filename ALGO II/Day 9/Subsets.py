class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        bag = []
        res = []
        start = 0
        n = len(nums)
        def backtrack(bag, start):
            res.append(bag.copy())
            for i in range(start, n):
                bag.append(nums[i])
                backtrack(bag, i + 1)
                bag.pop()    
        backtrack(bag, start)
        return res