class Solution(object):
    def reverseList(self, head):
       
        curr, prev = head, None
        
        while curr:
            curr_next = curr.next 
            curr.next = prev 
            curr, prev = curr_next, curr 
        
        return prev