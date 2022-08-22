class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dic = set()
        while headA:
            dic.add(headA)
            headA = headA.next
        while headB:
            if headB in dic:
                return headB
            headB = headB.next            
        return None