class Solution:
    def hasArrayTwoCandidates(self,arr, n, x):
        dict={}
        for i in arr:
            diff=x-i
            
            if diff in dict:
                return True
            dict[i]=i
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.hasArrayTwoCandidates(arr, n, x)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends
