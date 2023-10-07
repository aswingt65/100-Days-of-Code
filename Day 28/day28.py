import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self,grid):
        def dfs(l,m,visited):
            visited[l][m] = 1
            for i in range(-1,2):
                for j in range(-1,2):
                    if (l+i)>=0 and (m+j)>=0 and (l+i)<len(grid) and (j+m)<len(grid[0]):
                        if visited[l+i][m+j]!=1 and grid[l+i][m+j]==1:
                            dfs(l+i,m+j,visited)
                        
        visited = [[0]* len(grid[0]) for _ in range(len(grid))]
        count = 0
        for i in range(len(grid)) :
            for j in range(len(grid[0])):
                if visited[i][j]==0 and grid[i][j]==1 :
                    count += 1
                    dfs(i,j,visited)
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends
