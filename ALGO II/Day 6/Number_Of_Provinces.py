class Solution(object):
    def dfs(self,i,vis,isConnected):
        vis.add(i)
        for j in range(len(isConnected)):
            if(j not in vis and isConnected[i][j]==1):
                self.dfs(j,vis,isConnected)
                
    def findCircleNum(self, isConnected):
        vis=set()
        count=0
        for i in range(len(isConnected)):
            if(i not in vis):
                self.dfs(i,vis,isConnected)
                count+=1
        return count