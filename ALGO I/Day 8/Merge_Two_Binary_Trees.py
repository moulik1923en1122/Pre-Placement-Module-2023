class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        root3 = TreeNode()
        if root1 is not None and root2 is not None:
            root3.val = root1.val + root2.val
            root3.left = self.mergeTrees(root1.left,root2.left)
            root3.right = self.mergeTrees(root1.right,root2.right)        
        elif root1 is not None:
            root3.val = root1.val
            root3.left = self.mergeTrees(root1.left,root2)
            root3.right = self.mergeTrees(root1.right,root2)        
        elif root2 is not None:
            root3.val = root2.val
            root3.left = self.mergeTrees(root1,root2.left)
            root3.right = self.mergeTrees(root1,root2.right)
        else:
            return None
        
        return root3