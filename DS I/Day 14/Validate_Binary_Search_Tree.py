class Solution:
	def isValidBST(self, root: Optional[TreeNode]) -> bool:
		lst = []

		def inOrder(node,lst):
			if not node: return
			inOrder(node.left,lst)
			lst.append(node.val)
			inOrder(node.right,lst)

		inOrder(root,lst)
		for i in range(len(lst)-1):
			if lst[i+1]-lst[i] <= 0:
				return False
		return True