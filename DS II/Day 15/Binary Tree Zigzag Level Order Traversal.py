class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level  = 0 
        queue = deque([(root)])
        ans = []
        
        while queue:
            size = len(queue)
            level_nodes = []
            for _ in range(size):
                curr = queue.popleft()
        
                level_nodes.append(curr.val)        
                
                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
            
          
            if level % 2 == 1:
                level_nodes.reverse()
                
            level += 1
            ans.append(level_nodes)
        
        return ans