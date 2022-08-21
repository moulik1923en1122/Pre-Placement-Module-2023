class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        res = self.helper(root, res)
        return res
        
    def helper(self, root, res):
        if root:
            res = self.helper(root.left, res)
            res.append(root.val)
            res = self.helper(root.right, res)
          
        return res
