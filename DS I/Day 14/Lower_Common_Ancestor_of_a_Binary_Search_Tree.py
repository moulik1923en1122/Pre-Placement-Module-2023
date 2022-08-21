class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p, q = min(p.val, q.val), max(p.val, q.val)
        if root.val < p: return self.lowestCommonAncestor(root.right, TreeNode(p), TreeNode(q))
        if root.val > q: return self.lowestCommonAncestor(root.left, TreeNode(p), TreeNode(q))
        return root