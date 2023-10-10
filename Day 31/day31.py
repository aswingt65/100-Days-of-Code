def isValid(s):
    a=s.split('.')
    if(len(a)!=4):
        return 0
    for i in a:
        if len(i)>1 and i[0]=='0':
            return 0
        try:
            i=int(i)
            if 0<=i<=255:
                continue
            else:
                return 0
        except ValueError:
            return 0
    return 1

#{ 
 # Driver Code Starts
   
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        if(isValid(s)):
            print(1)
        else:
            print(0) 

# } Driver Code Ends
