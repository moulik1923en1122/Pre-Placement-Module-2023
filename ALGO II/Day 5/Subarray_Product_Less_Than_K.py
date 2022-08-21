class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        c=0
        pro=1
        while(i<len(nums)):
            pro=pro*nums[j]
            if(pro<k):
                c=c+1+j-i
                j=j+1
            else:
                if(i!=j):
                    pro=pro//(nums[i]*nums[j])
                    i=i+1
                else:
                    pro=pro//(nums[i])
                    i=i+1
                    j=i
            if(j==len(nums)):
                break
        return c 