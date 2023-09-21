class Solution:
    def countTriplet(self, arr, n):
        count=0
        s=set(arr)
        for i in range(n):
            for j in range(i+1,n):
                if arr[i]+arr[j] in s:
                    count+=1
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.countTriplet(arr, n)
		print(ans)

# } Driver Code Ends
