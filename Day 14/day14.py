class Solution:
    def pushZerosToEnd(self,arr, n):
        count=0
        for i in range(n):
            if arr[i]!=0:
                arr[count]=arr[i]
                count+=1
        for i in range(count,n):
            arr[i]=0
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends
