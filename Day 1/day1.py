#Remove duplicate elements from sorted Array

class Solution:    
    def remove_duplicate(self, A, N):
        i=0
        for j in range(1,len(A)):
            if(A[j]!=A[i]):
                A[i+1]=A[j]
                i+=1
        return i+1

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()
# } Driver Code Ends
