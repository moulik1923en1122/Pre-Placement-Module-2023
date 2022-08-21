class Solution:
#     code to check if a node is completely equal to another:
    def isEqual(self, root, subRoot):
        if root is None and subRoot is None:
            return True
            
        return root is not None and subRoot is not None and root.val == subRoot.val and self.isEqual(root.left, subRoot.left) and self.isEqual(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        if self.isEqual(root, subRoot):
            return True
        else:
#             check for the left and right nodes of root
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
			