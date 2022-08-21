class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)        
        def helper(self, node, path):            
            if node is None:
                return                                       
            path.append(node)   
            if node == n-1:                
                self.results+=[path.copy()]                
            for i in graph[node]:
                helper(self, i, path)
                path.pop()   
                            
            
        self.results = []
        helper(self,0, [] )
        return self.results
        