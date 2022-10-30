# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
inf = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = graph = [[] for _ in range(n)]

for _ in range(m):
    st, ed = map(int, input().split())
    graph[st-1].append(ed-1)
    graph[ed-1].append(st-1)
    

def get_smallest_node(distance, visited):
    min_value = inf
    index = 0
    for i in range(n):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index
    
def dijkstra(start):
    distance = [inf] * (n)
    visited = [False] * (n)
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i] = 1

    for _ in range(n-1):
        now = get_smallest_node(distance, visited)
        visited[now] = True

        for next in graph[now]:
            cost = distance[now] + 1
            if cost < distance[next]:
                distance[next] = cost

    return max(distance)

point = inf
idx = 0
for i in range(n):
    tmp = dijkstra(i)
    if point > tmp:
        point = tmp
        idx = i+1
    
print(idx)