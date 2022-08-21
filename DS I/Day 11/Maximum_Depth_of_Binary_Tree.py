class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            queue = [root]
            level = 0
            n = 1
            while len(queue) > 0:
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                n -= 1
                if n == 0:
                    level += 1
                    n = len(queue)
        return level