class Solution:
    def f(self,node,arr,x):
        if node==None:
            return False
        arr.append(node)
        if node.data==x:
            return True
        if self.f(node.left,arr,x) or self.f(node.right,arr,x):
            return True
        arr.pop(-1)
        return False
    def lca(self,root, n1, n2):
        # Code here
        arr1=[]
        if root==None:
            return arr1
        arr2=[]    
        self.f(root,arr1,n1)
        self.f(root,arr2,n2)
        ans=root
        for i in range(min(len(arr1),len(arr2))):
            if arr1[i]==arr2[i]:
                ans=arr1[i]
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        a,b=list(map(int,input().split()))
        s=input()
        root=buildTree(s)
        k=Solution().lca(root,a,b)
        print(k.data)

# } Driver Code Ends
