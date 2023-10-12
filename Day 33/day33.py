from collections import deque

class Solution:    
    def max_of_subarrays(self,arr,n,k):
        l = deque()
        ans_arr = []
        for i in range(n):
            if len(l) == 0:
                l.append(i)
            while(len(l) > 0 and i-l[0]>=k):
                l.popleft()
            while(len(l)>0 and arr[i] > arr[l[-1]]):
                l.pop()
            l.append(i)
            if i>=k-1:
                ans_arr.append(arr[l[0]])
            
        return (ans_arr)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends
