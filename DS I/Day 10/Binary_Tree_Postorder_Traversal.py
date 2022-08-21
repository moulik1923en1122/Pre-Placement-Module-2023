class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return root
        stack=[root]
        stack2=[]
        ans=[]
        
        while stack!=[]:
            node=stack.pop()
            stack2.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        
        while stack2!=[]:
            ans.append(stack2.pop())
            
        return ans