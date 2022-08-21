class Solution(object):
    def backspaceCompare(self, s, t):
        
        s1=[]    
        t1=[]   
        for i in s:
            if i.isalpha():
                s1.append(i)
            elif len(s1)==0:  
                continue
            else:
                s1.pop(-1)   
        for i in t:               
            if i.isalpha():
                t1.append(i)
            elif len(t1)==0:
                continue
            else:
                t1.pop(-1)
        
        while len(s1)==len(t1):
            return tuple(t1)==tuple(s1)