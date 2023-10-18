class Solution:
    def buildtree(self, inorder, preorder, n):
        if inorder:
            root=Node(preorder.pop(0))
            index=inorder.index(root.data)
            root.left=self.buildtree(inorder[:index],preorder,n)
            root.right=self.buildtree(inorder[index+1:],preorder,n)
            return root

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        inorder = [ int(x) for x in input().split() ]
        preorder = [ int(x) for x in input().split() ]
        
        root = Solution().buildtree(inorder, preorder, n)
        printPostorder(root)
        print()

# } Driver Code Ends
