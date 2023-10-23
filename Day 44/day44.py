def isSafe(graph, c, v, color, V):
    for i in range(V):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def isColored(graph, v, V, m, color):
    if v == V:
        return True
    
    for c in range(1, m + 1):
        if isSafe(graph, c, v, color, V):
            color[v] = c
            if isColored(graph, v + 1, V, m, color):
                return True
            color[v] = 0
    return False

def graphColoring(graph, m, V):
    color = [0] * V
    
    if isColored(graph, 0, V, m, color):
        return 1
    return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends
