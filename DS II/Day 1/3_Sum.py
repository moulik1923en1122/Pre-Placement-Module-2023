class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res= []
        
        if len(nums)<3 or nums[0]>0 or nums[-1]<0:
            return res
        
        
        for i in range(len(nums)-2):
            
            
            if i>0 and nums[i-1]==nums[i]:
                continue
            
            l = i+1
            r = len(nums)-1
            while l<r: 
                sum_3 = nums[i]+nums[l]+nums[r]
                
                if sum_3<0:
                    l+=1
               
                elif sum_3>0:
                    r-=1
                
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    
                    
                   
                    while l<r and nums[l] == nums[l-1]:
                    
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
        return res