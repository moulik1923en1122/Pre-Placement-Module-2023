class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        prev = TreeNode(root.val-1)
        prev.right = root
        return_root = prev
        
        while root and root.val != key:
            prev = root
            if root.val < key:
                root = root.right
            else:
                root = root.left
        
        if root is not None:
            if prev.left and prev.left.val == key:
                if root.right is None:
                    prev.left = root.left
                else:
                    prev.left = root.right
                    right_subtree = root.right
                    while right_subtree.left:
                        right_subtree = right_subtree.left
                    right_subtree.left = root.left
            elif prev.right and prev.right.val == key:
                if root.left is None:
                    prev.right = root.right
                else:
                    prev.right = root.left
                    left_subtree = root.left
                    while left_subtree.right:
                        left_subtree = left_subtree.right
                    left_subtree.right = root.right

        return return_root.right