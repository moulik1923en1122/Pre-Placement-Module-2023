class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        def reverseInterval(startIndex, length):
            l, r = startIndex, startIndex+length-1
            if r >= len(nodes):
                return
            while l<r:
                nodes[l], nodes[r] = nodes[r], nodes[l]
                l+=1
                r-=1
        i = 0
        while i < len(nodes):
            reverseInterval(i, k)
            i+=k

        cur, newHead = nodes[0], nodes[0]
        for i in range(1, len(nodes)):
            cur.next = nodes[i]
            cur = cur.next
        cur.next = None
        return newHead