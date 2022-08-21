class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr=head
        while(curr!=None):
            if(curr==head and curr.val==val):
                head=curr.next
                curr=curr.next
            elif(curr.next and curr.next.val==val):
                curr.next = curr.next.next
            else:
                curr=curr.next

        return head