import sys
from itertools import permutations
input = sys.stdin.readline

move = [(0,1),(1,0),(-1,0),(0,-1)]
def search(start, end):
    count_graph = [[0 for i in range(m)] for i in range(n)]
    need_visited, visited = [start], []
    end = {i: -1 for i in end}
    point = len(end)

    while need_visited:
        if point == 0:
            break
        
        x, y = need_visited.pop()
        if (x,y) not in visited:
            visited.append(x,y)
            for x_, y_ in move:
                mx, my = x+x_, y+y_
                
                if (0 <= mx < n) and (0 <= my < m):
                    if graph[mx][my] != 'X':
                        count_graph[mx][my] = count_graph[x][y] + 1
                        need_visited.append((mx, my))
                        if graph[mx][my] == 'P':
                            point -= 1
                            end[(mx,my)] = count_graph[mx][my]

    return max(list(end.values()))


n, m = map(int, input().split())

graph = []
start, end = [], []
for i in range(n):
    tmp = list(input().strip())
    graph.append(tmp)
    end.extend([(i,idx) for idx,j in enumerate(tmp) if j == 'P'])
    start.extend([(i,idx) for idx,j in enumerate(tmp) if j == 'C'])

result = []
for st in start:
    result.append(search(st, end))

# point = int(1e9)
# item = list(permutations(list(range(len(start))), len(start)))
# print(item)
# print(result)
# for i in item:
#     tmp = 0
#     print(list(zip(i,result)))
#     for idx, r in zip(i,result):
#         tmp = max(tmp, r[idx])

#     point = min(point, tmp)

print(min(result))
