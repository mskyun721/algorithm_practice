# 단순 dfs
def dfs(graph, start):
    need_visited, visited = [start], []

    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            need_visited.extend(graph[node])
            visited.append(node)
    
    return visited

# 단순 bfs
def bfs(graph, start):
    need_visited, visited = [start], []

    while need_visited:
        node = need_visited[0]
        del need_visited[0]

        if node not in visited:
            need_visited.extend(graph[node])
            visited.append(node)
    
    return visited

# dfs 전체 경로 / 경로의 수
cnt = 0
path = []
def dfs_root(graph, start, end):
    global cnt, path
    tmp = []
    visited = [[True for _ in range(len(graph[0])) for _ in range(len(graph))]]
    if start == end:
        cnt += 1
        path.append(tmp)
    
    else:
        for i in graph[start]:
            if visited[i]:
                visited[i] = False
                tmp.append(i)
                dfs_root(graph, i, end)
                tmp.pop()
                visited[i] = True


# 다익스트라 알고리즘
# https://techblog-history-younghunjo1.tistory.com/247
# 시작노드와 노드간의 가중치가 존재 할때 
# 시작노드 부터 모든 노드에 대한 최단 경로를 구해주는 알고리즘

INF = int(1e9)
n, m = 0, 0


def min_node(d, v):
    min_value = INF
    idx = 0
    for i in range(1, n+1):
        # 방문하지 않은 노드이면서 시작 노드와 최단거리인 노드
        if not v[i] and d[i] < min_value:
            min_value = d[i]
            idx = i
    
    return idx

def dijkstra(graph, start):
    distance, visited = [INF for _ in range(n+1)], [False for _ in range(n+1)]
    distance[start] = 0
    visited[start] = True

    # start node와 직접 연결된 node의 거리(가중치)
    for r, d in graph[start]:
        distance[r] = d

    # start node를 제외한 노드의 최단거리
    for _ in range(n-1):
        idx = min_node(distance, visited)
        visited[idx] = True
        for r, d in graph[idx]:            
            distance[r] = min(distance[r], distance[idx] + d)

# 다익스트라 알고리즘 heapq ( 복잡도 감소 )
# https://techblog-history-younghunjo1.tistory.com/248
# heapq : https://techblog-history-younghunjo1.tistory.com/241?category=868547
# min_node 함수로 진행하던 최단 거리의 노드 필요없이 heapq를 사용하면 자동으로 오름차순 정렬

import heapq

def disjkstra_hq(graph, start):
    distance, visited = [INF for _ in range(n+1)], []
    heapq.heappush(visited, (0, start))
    distance[start] = 0
    while visited:
        dist, node = heapq.heappop(visited)
        if distance[node] < dist:
            continue
            
        for r, d in graph[r]:
            distance[r] = min(distance[r], distance[r] + d)
            heapq.heappush(visited, (distance[r], r))


### 크루스칼 알고리즘 : https://techblog-history-younghunjo1.tistory.com/262
# 서로소 집합 자료구조 : 서로 공통 요소. 교집합이 없는 서로 다른 집합.
# https://techblog-history-younghunjo1.tistory.com/257
# [1,2], [4,5] = 서로소 집합 O / [1,2], [2,4] = 서로소 집합 X
# 서로소 집합 자료구조는 합집합(union)과 찾기(find) 연산으로 이루어져 있다.
# 두 연산을 통해 집합 간의 공통 요소가 있는지 판별할 수 있다.
# 서로소 집합 : root noed 찾기

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    parent[max(a,b)] = min(a,b)

# n = 6
# parent = [i for i in range(n+1)]
# for a,b in [(1,2), (2,3), (4,1), (6,5)]:
#     print(f'a,b : {a,b}')
#     union_parent(parent, a, b)
#     print(f'parent : {parent}')

# # parent 값이 모드 같은 root 이면 cycle 형성된 graph
# n = 7
# parent = [i for i in range(n+1)]
# for a,b in [(1,2), (1,5), (2,3), (2,6), (3,4), (4,7), (5,6), (6,4), (7,6)]:
#     print(f'a,b : {a,b}')
#     union_parent(parent, a, b)
#     print(f'parent : {parent}')

# 최소 신장 트리 : 모든 노드를 포함하면서 모든 노드간의 사이클이 존재하지 않는 그래프
# 크루스칼 알고리즘은 최소 신장 트리를 찾는 알고리즘이다. 
# 즉, 모든 노드를 포함하면서 사이클이 존재하지 않는 최소 트리를 찾는다.

