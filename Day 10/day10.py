import heapq

class Solution:
    def minCost(self,arr,n) :
        heapq.heapify(arr)
        sum = 0
        while len(arr) > 1:
            x = heapq.heappop(arr)
            y = heapq.heappop(arr)
            sum += x+y
            heapq.heappush(arr, x+y)
        return sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import  defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minCost(a,n))
# } Driver Code Ends
