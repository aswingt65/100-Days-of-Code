import heapq 

class Solution:
    def spanningTree(self, V, adj):
        res = 0
        visited=set()
        minH=[(0,0)]
        while minH:
            cur_c,cur_n =heapq.heappop(minH)
            if cur_n in visited :
                continue
            res += cur_c
            visited.add(cur_n)
            for n,c in adj[cur_n]:
                if n not in visited:
                    heapq.heappush(minH,(c,n))
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends
