def findElement( arr, n):
    for i in range(1,n-1):
        l=0
        m=0
        ele=arr[i]
        for j in range(0,i):
            if(arr[j]<=ele):
                l+=1
            else:
                break 
        for k in range(i+1,n):
            if(arr[k]>=ele):
                m+=1
            else:
                break 
        if(l+m==n-1):
            return ele
    return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
    T = int(input())
    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(findElement(a, n))

        T -= 1

if __name__ == "__main__":
    main()
    
# } Driver Code Ends
