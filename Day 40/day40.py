class Solution:
    def eggDrop(self,n, k):
        dp = {}
        def bt(n, k):
            if (n, k) in dp:
                return dp[(n, k)]
            if k == 1 or k == 0 or n == 1:
                return k
            ans = float("inf")
            for i in range(1, k + 1):
                res = max(bt(n - 1, i - 1), bt(n, k - i))
                ans = min(ans, res)
            dp[(n, k)] = ans + 1
            return ans + 1
        return bt(n, k)

#{ 
 # Driver Code Starts
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k = map(int,input().strip().split())
        ob=Solution()
        print(ob.eggDrop(n,k))
# } Driver Code Ends
