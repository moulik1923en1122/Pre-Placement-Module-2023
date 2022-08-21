class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        bag = []
        res = []
        start = 0
        n = len(nums)
        nums.sort()
        used = [False for _ in range(n)]
        def backtrack(bag, start):
            res.append(bag.copy())
            for i in range(start, n):
                if i == 0 or nums[i] != nums[i - 1] or used[i - 1] == True:
                    used[i] = True
                    bag.append(nums[i])
                    backtrack(bag, i + 1)
                    bag.pop()
                    used[i] = False
        backtrack(bag, start)
        return res