class Solution:

    def minStepToReachTarget(self, KnightPos, TargetPos, n):
        hx,hy=KnightPos[0]-1,KnightPos[1]-1
        tx,ty=TargetPos[0]-1,TargetPos[1]-1
        
        visited={(hx,hy):1}
        q=[[hx,hy,0]]
        
        while q:
            x,y,d=q.pop(0)
            if x==tx and y==ty:
                return d
            for i,j in [[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]:
                r,c=x+i,y+j
                if 0<=r<n and 0<=c<n and (r,c) not in visited:
                    q.append([r,c,d+1])
                    visited[(r,c)]=1
        
        return -1

#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	N = int(input())
	KnightPos = list(map(int, input().split()))
	TargetPos = list(map(int, input().split()))
	obj = Solution()
	ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
	print(ans)

# } Driver Code Ends
