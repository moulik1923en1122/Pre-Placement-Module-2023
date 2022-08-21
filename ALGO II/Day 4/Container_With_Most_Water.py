class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        ans = 0
        
        while left < right :
            
            ans = max(ans, min(height[left], height[right]) * (right-left))
            
            if height[left] > height[right] :
                right -= 1
            else :
                left += 1
        
        return ans