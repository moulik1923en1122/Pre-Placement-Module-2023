class Node:
    
    def __init__(self, val=None):
        self.val = val
        self.minval = val
        self.next = None

class LinkedList:
    
    def __init__(self):
       
        self.head = Node()
       
        self.length = 0
        
    def pop(self):
      
        if self.length:
          
            to_remove = self.head.next 
            
            self.head.next = to_remove.next
            
            self.length -= 1
            
    def push(self, val):
        
        to_add = Node(val)
        
        old_val = self.head.next 
       
        if old_val:
            if old_val.minval < val:
                to_add.minval = old_val.minval
        
        self.head.next = to_add
        
        to_add.next = old_val
        
        self.length += 1
        
    def top(self):
        
        return self.head.next
        
        


class MinStack:

    def __init__(self):
        self.stack = LinkedList()

    def push(self, val: int) -> None:
        self.stack.push(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack.top().val

    def getMin(self) -> int:
        return self.stack.top().minval