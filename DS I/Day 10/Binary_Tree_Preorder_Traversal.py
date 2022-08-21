class Solution:
    def preorderTraversal(self, node: Optional[TreeNode]) -> List[int]:
        if node:
            yield node.val
            yield from self.preorderTraversal(node.left)
            yield from self.preorderTraversal(node.right)