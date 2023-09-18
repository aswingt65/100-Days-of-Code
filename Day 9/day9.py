class Solution:
    def insert(self, alist, index, n):
        pass
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        i=0
        for j in range(1,n):
            key=arr[j]
            i=j-1
            while i>=0 and key<arr[i]:
                arr[i+1]=arr[i]
                i=i-1
            arr[i+1]=key
        return arr
                
#{ 
 # Driver Code Starts

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends
