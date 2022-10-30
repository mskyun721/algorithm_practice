import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
start, end = [], []
for i in range(n):
    tmp = list(input().strip())
    graph.append(tmp)
    for j in range(m):
        if tmp[j] == 'P':
            end.append((i,j))
        elif tmp[j] == 'C':
            start.append((i,j))


move = [(0,1),(1,0),(-1,0),(0,-1)]
def search(start):
    count_graph = [[0 for i in range(m)] for i in range(n)]
    need_visited, visited = [start], []
    point = 0

    while need_visited:
        if point == len(end):
            break
        x, y = need_visited.pop()

        if (x, y) not in visited:
            visited.append((x, y))
            for i in range(4):
                mx, my = x+move[i][0], y+move[i][1]
                    
                if (0 <= mx < n) and (0 <= my < m):
                    if graph[mx][my] != 'X':
                        count_graph[mx][my] = count_graph[x][y] + 1
                        need_visited.append((mx, my))
                
                        if graph[mx][my] == 'P':
                            point += 1

    result = []
    for x, y in end:
        result.append(count_graph[x][y])

    return result


result = []
for i, st in enumerate(start):
    result.append(search(st))

point = -1
item = list(permutations(list(range(len(start))), len(start)))
for i in item:
    tmp = []
    for idx, r in zip(i,result):
        tmp.append(r[idx])

    if point < 0:
        point = max(tmp)
    else:
        point = min(point, max(tmp))

print(point)






