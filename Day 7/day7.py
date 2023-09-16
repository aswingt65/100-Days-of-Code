class Solution:
    def findUnion(self,a,b,n,m):
        A = set(a)
        B = set(b)
        C = A.union(B)
        l = list(C)
        l.sort()
        return l

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        li = ob.findUnion(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends
