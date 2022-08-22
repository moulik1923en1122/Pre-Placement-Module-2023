

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        node = head

        head = tail = ListNode()

        i = 0

        while node:

            if i % 2 == 0:

                if node.next:

                    tail.next = ListNode(node.next.val, ListNode(node.val))

                    tail = tail.next.next

                else:

                    tail.next = ListNode(node.val)

                    tail = tail.next

            i, node = i + 1, node.next

        return head.next