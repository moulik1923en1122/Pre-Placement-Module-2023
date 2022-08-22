class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        values = {}
        while True:
            if not head.next:
                return
            values[id(head)] = head
            node_by_id = values.get(id(head.next))
            if node_by_id:
                return node_by_id
            head = head.next