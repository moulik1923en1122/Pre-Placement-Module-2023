class Solution(object):
	def deleteDuplicates(self, head):
		curr,prev = head,None
		seen = None
		while curr is not None:
			if curr.next is not None and curr.val == curr.next.val:
				seen = curr.val
			if curr.val == seen:
				if not prev:
					head = curr.next
				else:
					prev.next = curr.next
				curr=curr.next
				continue
			prev=curr
			curr = curr.next
		return head