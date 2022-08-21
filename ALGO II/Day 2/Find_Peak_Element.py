class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=len(nums)
        b=1
        e=l-1
        if(l==1):
            return 0
        elif(nums[0]>nums[1]):
            return 0
        elif(nums[l-1]>nums[l-2]):
            return l-1
        while(b<=e):
            if(nums[b]>nums[b-1] and nums[b]>nums[b+1]):
                return b
            else:
                b+=1
            if(nums[e]>nums[e-1] and nums[e]>nums[e+1]):
                return e
            else:
                e-=1