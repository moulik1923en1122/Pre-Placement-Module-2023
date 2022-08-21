class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        bag = []
        res = []
        n = len(nums)
        nums.sort()
        used = [False for _ in range(n)]
        def backtrack(bag, used):
            if len(bag) == n:
                res.append(bag.copy())
                return
            for i in range(n):
			    # in the case of nums containing duplicates
                if used[i] == False and (i==0 or nums[i] != nums[i-1] or used[i-1] == True):
                    bag.append(nums[i])
                    used[i] = True
                    backtrack(bag, used)
                    used[i] = False
                    bag.pop()
        backtrack(bag, used)
        return res
