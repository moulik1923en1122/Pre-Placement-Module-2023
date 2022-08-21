class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = []
        res = []
        while root or s:
            if root:
                s.append(root)
                root = root.left
            else:
                root = s.pop()
                res.append(root.val)
                root = root.right
        
        d = {}
        for i in res:
            if (k - i) in d:
                return True
            else:
                d[i] = 1
        
        return False