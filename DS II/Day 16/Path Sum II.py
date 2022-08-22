class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, targetSum, path):
            if not root:
                return
            targetSum -= root.val
            path.append(root.val)
            if not root.left and not root.right and not targetSum:
                    ans.append(path.copy())
            else:
                dfs(root.left, targetSum, path)
                dfs(root.right, targetSum, path)
            path.pop()

        ans = []
        dfs(root, targetSum, [])
        return ans