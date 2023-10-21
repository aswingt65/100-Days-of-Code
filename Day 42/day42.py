class Solution:
    def maxGold(self, n, m, M):
        dp=[[None for _ in range(m)] for _ in range(n)]
        for r in range(n):
            dp[r][m-1]=M[r][m-1]
        for c in range(m-2,-1,-1):
            for r in range(n):
                ans=0
                if r>0:
                    ans=max(ans,dp[r-1][c+1])
                ans=max(ans,dp[r][c+1])
                if r<n-1:
                    ans=max(ans,dp[r+1][c+1])
                dp[r][c]=ans+M[r][c]
        res=0
        for r in range(n):
            res=max(res,dp[r][0])
        return res

#{ 
 # Driver Code Starts

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        tarr = [int(x) for x in input().split()]
        M = []
        j = 0
        for i in range (n):
            M.append(tarr[j:j + m])
            j = j+m
        
        ob = Solution()
        print(ob.maxGold(n, m, M))
      
# } Driver Code Ends
