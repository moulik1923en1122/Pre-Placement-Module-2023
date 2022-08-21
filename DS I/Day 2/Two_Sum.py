from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        df = defaultdict(lambda:-1)
        
        for idx,val in enumerate(nums):
            if df[target-val]!=-1:
                return [df[target-val],idx]
            else:
                df[val]=idx
            