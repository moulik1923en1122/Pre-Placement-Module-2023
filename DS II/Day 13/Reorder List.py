class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        vals = list()
        dummy = head
        
        while dummy:
            vals.append(dummy.val)
            dummy = dummy.next
        
        i = 0
        j = len(vals) - 1
        dummy = head
        
        while i <= j:
            dummy.val = vals[i]
            i += 1
            if dummy.next:
                dummy = dummy.next
                dummy.val = vals[j]
                j -= 1
                if dummy.next:
                    dummy = dummy.next
            else: 
                break
        
        return head