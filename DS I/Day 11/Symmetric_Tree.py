class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def solve(lroot, rroot):
            if lroot == None or rroot == None:
                return lroot == rroot
            if lroot.val != rroot.val:
                return False
            return solve(lroot.left, rroot.right) and solve(lroot.right, rroot.left)
        return solve(root.left, root.right)