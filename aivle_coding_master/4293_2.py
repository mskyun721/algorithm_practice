import sys
input = sys.stdin.readline
INF = int(sys.maxsize)

n, m = map(int, input().split())
graph = {i : [] for i in range(1,n+1)}

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


