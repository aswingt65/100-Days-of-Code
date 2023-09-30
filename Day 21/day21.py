class Solution:
    
    def findMaxSum(self,arr, n): 
        dp = [-1 for i in range(n)] 
        prev = arr[0] 
        prev2 = 0
        for i in range(1, n): 
            select = arr[i]
            if i > 1: 
                select += prev2 
                
            notselect = 0 + prev 
            cur = max(select, notselect)
            prev2 = prev 
            prev = cur 
            
        return prev

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1
# } Driver Code Ends
