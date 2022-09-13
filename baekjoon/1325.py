### 효율적인 해킹 silver 1
# n : 회사 수
# m : 신뢰 관계 수
# a b : a는 b를 신뢰한다
# b회사를 해킹하면 a회사도 해킹 할 수 있다

import sys
from collections import deque
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
company = defaultdict(list)


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    company[b].append(a)


def bfs(graph, start_node):
    visited = [0] * (n+1)
    need_visited = deque([start_node])

    visited[start_node] = 1
    cnt = 0
    
    while need_visited:
        node = need_visited.pop()
        cnt += 1
        for g in graph[node]:
            if not visited[g]:
                need_visited.append(g)
                visited[g] = 1
    
    return cnt
    
count = []
for i in range(1, n+1):
    count.append([bfs(company, i), i])

count.sort(key=lambda x:(-x[0], x[1]))
maxlen = count[0][0]

for value, key in count:
    if value == maxlen:
        print(key, end=' ')
    else:
        break