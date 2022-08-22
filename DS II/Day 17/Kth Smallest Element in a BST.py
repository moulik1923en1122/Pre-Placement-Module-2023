class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k=k
        self.ans=0
        def form_list(root):
            if(root):
                form_list(root.left)
                self.k-=1
                if(self.k==0):
                    self.ans=root.val
                    return
                form_list(root.right)
        form_list(root)
        return self.ans