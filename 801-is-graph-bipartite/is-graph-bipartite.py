class Solution:
    def dfs(self,current_node,visited,graph,color):
        visited[current_node]=color
        for adjNode in graph[current_node]:
            if visited[adjNode]!= -1:
                if visited[adjNode]==color:
                    return False
            else:
                if color==0:
                    ans=self.dfs(adjNode,visited,graph,1)
                else:
                    ans=self.dfs(adjNode,visited,graph,0)
                if ans == False:
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        visited=[-1]*n
        for i in range(0,n):
            if visited[i]==-1:
                ans=self.dfs(i,visited,graph,0)
                if ans == False:
                    return False
        return True
