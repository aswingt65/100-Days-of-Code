import heapq
class Solution:
    def dijkstra(self, V, adj, S):
        result = [100000000]*V
        pq = [[0,S]]
        result[S] = 0
        heapq.heapify(pq)
        while(pq):
            val = heapq.heappop(pq)
            distance = val[0]
            node = val[1]
            for i in adj[node]:
                adjNode = i[0]
                adjWeight = i[1]
                if(distance+adjWeight < result[adjNode]):
                    result[adjNode] = distance+adjWeight
                    pq.append([result[adjNode],adjNode])
        return result

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
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends
