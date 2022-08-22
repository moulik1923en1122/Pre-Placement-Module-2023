class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
         
	
        nb1, nb2 = "", ""
		
        while l1 is not None or l2 is not None :
            if l1 :
                nb1 = str(l1.val) + nb1
                l1 = l1.next
            if l2 :
                nb2 = str(l2.val) + nb2
                l2 = l2.next
				
        res = int(nb1) + int(nb2)
        ans = ListNode(0)
        l = ans
		
        while True:
            l.next = ListNode(res%10)
            l = l.next
            res = res // 10
            if res == 0 :
                break
				
        return ans.next