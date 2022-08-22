class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        def topo(node,visited,s):
            visited[node] = True
            for neighbour in g[node]:
                if not visited[neighbour]:
                    topo(neighbour,visited,s)
            s += [node]
            return
        def visit(node,visited):
            visited[node] = True
            for neighbour in g[node]:
                if not visited[neighbour]:
                    visit(neighbour,visited)
            return
        g = [[] for _ in range(n)]
        for i,j in edges:
            g[i] += [j]
        
        visited = [False for _ in range(n)]
        s = []
        for i in range(n):
            if not visited[i]:
                topo(i,visited,s)
        visited = [False for _ in range(n)]
        nodes = []
        while s:
            curr = s.pop()
            if not visited[curr]:
                visit(curr,visited)
                nodes += [curr]
        return nodes