import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(sys.maxsize)
graph = [[] for i in range(n+1)]

for _ in range(m):
    st, ed, d = map(int, input().split())
    graph[st].append((ed, d))

def dijkstra(start):
    distance, visited = [INF] * (n+1), []
    heapq.heappush(visited, (start, 0))
    distance[start] = 0

    while visited:
        node, dist = heapq.heappop(visited)

        if distance[node] < dist:
            continue

        for i, d in graph[node]:
            if distance[i] > (distance[node] + d):
                distance[i] = distance[node] + d
                heapq.heappush(visited, (i, distance[i]))
    
    return distance

for i in range(1, n+1):
    tmp = dijkstra(i)
    for j in tmp[1:]:
        if j == INF:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()


