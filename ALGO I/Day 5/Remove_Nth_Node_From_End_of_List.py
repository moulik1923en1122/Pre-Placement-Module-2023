class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        temp = ListNode()
        temp.next = head
        fast = temp
        slow = temp
        
        for i in range(1,n+1):
            fast = fast.next
            
        while fast.next != None:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return temp.next