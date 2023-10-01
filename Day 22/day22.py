class Solution:
    def maxLen(self,arr, N):
        length={0:-1}
        count=0
        max_len=0
        
        for i in range(N):
            if arr[i] == 0:
                count -= 1
            else:
                count += 1
            if count in length:
                max_len = max(max_len,i-length[count])
            else:
                length[count] = i
                
        return max_len


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().maxLen(a, len(a))
    print(s)
# } Driver Code Ends
