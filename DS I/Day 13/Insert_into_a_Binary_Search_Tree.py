class Solution(object):
    def insertIntoBST(self, root, val):
        nodeToInsert = TreeNode(val)
        if not root:
            return nodeToInsert
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
            return root
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
            return root  