class Solution:
    def nextPermutation(self, N, a):
        k=-1
        for j in range(N-2,-1,-1):
            if a[j]<a[j+1]:
                k=j
                break
        if k==-1:
            a=a[::-1]
            return a
        for j in range(N-1,k,-1):
            if a[j]>a[k]:
                t=a[j]
                a[j]=a[k]
                a[k]=t
                break
        l=a[k+1:]
        l=l[::-1]
        a[k+1:]=l
        return a

#{ 
 # Driver Code Starts

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends
