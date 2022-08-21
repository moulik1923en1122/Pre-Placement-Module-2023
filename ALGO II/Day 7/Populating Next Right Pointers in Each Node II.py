class Solution:
    def connect(self, root: 'Node') -> 'Node':
        d = defaultdict(list)
        
        stack = [(root, 0)]
        
        while stack:
            node, depth = stack.pop()
            if node:
                d[depth].append(node)
                if node.right:
                    stack.append((node.right, depth + 1))
                if node.left:
                    stack.append((node.left, depth + 1))
      
        for k in d:
            arr = d[k]

          
            for i in range(len(arr)-1):
        
                arr[i].next = arr[i+1]
            arr[-1].next = None
         
        return root