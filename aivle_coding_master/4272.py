import sys
input = sys.stdin.readline

n = int(input())
MAP = []
arr = [[[0,0] for _ in range(n)] for _ in range(n)]
for _ in range(n):
    MAP.append(list(map(int, input().split())))


move = [(1,0),(0,1)]
result = []
def dfs(graph, arr, start, end):
    global result
    print(start)
    
    if start == end:
        print(f'result : {arr[n-1][n-1]}')
        result.append(arr[n-1][n-1])
    else:
        for x, y in move:
            nx, ny = x+start[0], y+start[1]
            if 0 <= nx < n and 0 <= ny < n:
                print(arr[x][y])
                arr[nx][ny][0] = arr[x][y][0] + 1
                arr[nx][ny][1] = arr[x][y][1] + graph[nx][ny]
                for i in arr:
                    print(i)
                dfs(graph, arr, (nx, ny), end)
                print('reset')
                arr[nx][ny][0] = 0
                arr[nx][ny][1] = 0



dfs(MAP, arr, (0,0), (n-1,n-1))
print(result)


