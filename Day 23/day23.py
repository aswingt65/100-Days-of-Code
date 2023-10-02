class Solution:
    def numberOfPaths(self, m, n):
       mod = 1000000007
       dp = [[0 for i in range(n+1)] for j in range(m+1)]
       dp[0][1] = 1
       for i in range(1,m+1):
           for j in range(1,n+1):
               dp[i][j] = (dp[i-1][j]%mod + dp[i][j-1]%mod)%mod
               
       return dp[m][n]%mod

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m,n = input().split()
		m=int(m)
		n=int(n)
		ob = Solution();
		print(ob.numberOfPaths(m,n))

# } Driver Code Ends
