class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
            
        
        output = head
        
        while head.next:
            
            if head.val == head.next.val:
                head.next = head.next.next
            
            else:
                head= head.next
        
        return output