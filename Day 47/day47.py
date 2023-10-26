def wordBreak(line, dictionary):

    n = len(line)
    dp = [0 for i in range(n+1)]
    
    dp[0] = True
    
    for i in range(n+1):
        for j in range(i):
            if dp[j] and line[j:i] in dictionary:
                dp[i] = True
                break
    
    return dp[n]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		dictionary = [word for word in input().strip().split()]
		line = input().strip()
		res = wordBreak(line, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends
