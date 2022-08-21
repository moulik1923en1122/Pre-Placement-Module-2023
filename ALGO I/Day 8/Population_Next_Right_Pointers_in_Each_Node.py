class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        dummy = root
        
       
        while root.left:
           
            next_level = root.left
            
            
            while root:
                root.left.next = root.right
                if root.next is not None:
                    root.right.next = root.next.left  
                root = root.next
            
           
            root = next_level
        return dummy