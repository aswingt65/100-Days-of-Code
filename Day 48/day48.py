from collections import deque,defaultdict
class Solution:
    
    def dfs(self,node,vis,adj,st):
        vis[node] = 1
        for adjNode in adj[node]:
            if vis[adjNode] == 0:
                self.dfs(adjNode,vis,adj,st)
        st.append(node)
        
    def dfs2(self,node,vis,adjRev):
        vis[node] = 1
        for adjNode in adjRev[node]:
            if vis[adjNode] == 0:
                self.dfs2(adjNode,vis,adjRev)
        
    def kosaraju(self, V, adj):
        st = deque()
        vis = [0]*V
        
        for i in range(V):
            if vis[i] == 0:
                self.dfs(i,vis,adj,st)
                
        adjRev = defaultdict(list)
        for v in range(V):
            vis[v] = 0
            for u in adj[v]:
                adjRev[u].append(v)
        
        scc = 0   
        while st:
            node = st.pop()
            if vis[node] == 0:
                vis[node] = 1
                scc += 1
                self.dfs2(node,vis,adjRev)
        
        return scc

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends
