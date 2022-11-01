from re import I
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(sys.maxsize)
graph = [[] for i in range(n+1)]

for _ in range(m):
    st, ed, d = map(int, input().split())
    graph[st].append([ed, d])


def min_node(distance, visited):
    min_value = INF
    idx = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i
    
    return idx

def dijkstra(start):
    visited, distance = [False] * (n+1), [INF] * (n+1)
    distance[start], visited[start] = 0, True

    for i in graph[start]:
        distance[i[0]] = i[1]
    
    for _ in range(n-1):
        idx = min_node(distance, visited)
        visited[idx] = True

        for i in graph[idx]:
            d = distance[idx] + i[1]
            if d < distance[i[0]]:
                distance[i[0]] = d

    return distance[1:]


for i in range(1, n+1):
    tmp = dijkstra(i)
    for j in tmp:
        if j == INF:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()


