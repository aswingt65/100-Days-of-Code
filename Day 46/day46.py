class Solution:
    def findSubString(self, str):
        distinct = len(set(str))
        dic = {}
        ans = len(str)
        i,j = 0,0
        while i<len(str):
            if str[i] in dic:
                dic[str[i]] += 1
            else:
                dic[str[i]] = 1
            if distinct == len(dic):
                while dic[str[j]] > 1:
                    dic[str[j]] -= 1
                    j += 1
                ans = min(ans,i-j+1)
            i += 1
        return ans

#{ 
 # Driver Code Starts

def main():

    T = int(input())

    while(T > 0):
    	str = input()
    	ob=Solution()
    	print(ob.findSubString(str))
    	
    	T -= 1

if __name__ == "__main__":
    main()

# } Driver Code Ends
