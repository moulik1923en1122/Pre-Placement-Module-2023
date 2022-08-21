class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        q=deque([root])
        while q:
            node=q.popleft()
            if node:
                if node.val==val:
                    return node
                q.append(node.left)
                q.append(node.right)
        return None