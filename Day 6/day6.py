def transitionPoint(arr, n):
    if 0 not in arr:
        return 0
    elif 1 not in arr:
        return -1
    for i in arr:
        if i==1:
            return arr.index(i)
            break
        
#{ 
 # Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))

# } Driver Code Ends
