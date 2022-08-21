class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(nums[-1] < nums[0]):          
            p1 = 0
            p2 = len(nums)-1
            while(p1 < p2):
                middle = (p2-p1)//2 + p1
                if(nums[middle] > nums[middle+1]):
                    return nums[middle+1]     #case - next number is minimum
                elif(nums[middle] < nums[p1]):
                    p2 = middle               #case - minimum is in left 
                elif(nums[middle] > nums[p1]):
                    p1 = middle + 1           #case - minimum is in right
                else:
                    return nums[middle]       #case - middle is minimum
        else:
            return nums[0]
        