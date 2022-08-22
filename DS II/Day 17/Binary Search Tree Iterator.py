class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        self.inorder_trav = [-1] + inorder(root)
        self.current = 0
		
    def next(self) -> int:
        self.current+=1
        return self.inorder_trav[self.current]

    def hasNext(self) -> bool:
        return self.current < len(self.inorder_trav) - 1