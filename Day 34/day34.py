class Solution:

    def checkTriplet(self,arr, n):
        squares = [x**2 for x in set(arr)]
        values = dict()
        for v in squares:
            values[v]=True
            
        for i in range(len(squares)):
            for j in range(i+1, len(squares)):
                if squares[i]+squares[j] in values:
                    return True
        return False

#{ 
 # Driver Code Starts

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.checkTriplet(arr, n)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends
