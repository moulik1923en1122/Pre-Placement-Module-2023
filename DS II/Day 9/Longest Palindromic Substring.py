class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
         
        if len(s) < 2:
            return s
        
        
   
        long_pal = [0,0]
    
        for idx, letter in enumerate(s):
             
            left_pal = self.checkPalindrome(s, idx, idx)
    
    
            left_pal_len = left_pal[1] - left_pal[0] + 1
    

            right_pal = self.checkPalindrome(s, idx, idx + 1) if (idx < len(s) - 1) and (s[idx] == s[idx+1]) else [idx, idx]
    

            right_pal_len = right_pal[1] - right_pal[0] + 1
    
    
    
    

            if (left_pal_len > right_pal_len) and (left_pal_len > (long_pal[1]-long_pal[0])):
                long_pal = left_pal
            
             
            elif (right_pal_len > left_pal_len) and (right_pal_len > (long_pal[1]-long_pal[0])):
                long_pal = right_pal



            if long_pal[1] == len(s) - 1:
                break

        
   
        return s[long_pal[0]:long_pal[1]+1]
    
    def checkPalindrome(self, s, l_idx, r_idx):
        while l_idx >= 0 and r_idx < len(s) and s[l_idx] == s[r_idx]:
            l_idx -= 1
            r_idx += 1           
        return [l_idx+1, r_idx -1]