class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = [0] * len(isConnected)
        count = 0
        for i in range(len(isConnected)):
            if self.visited[i] == 1:
                continue
            for j in range(len(isConnected)):
                if self.visited[j] == 0 and isConnected[i][j] == 1:                
                    self.visited[i] = 1
                    self.dfs_visit(isConnected, j)
                    count += 1
            
        return count
    
    def dfs_visit(self, isConnected, curr):
        for i in range(len(isConnected)):
            if isConnected[curr][i] == 1 and self.visited[i] == 0:
                self.visited[i] = 1
                self.dfs_visit(isConnected, i)
                
# [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
# [[1,0,0],[0,1,0],[0,0,1]]