import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
move = [(1,0),(0,1),(-1,0),(0,-1)]
road = []
for _ in range(n):
    road.append(list(input().strip()))

start, end = (0,0), (n-1, m-1)


def dfs_search_road(graph, start, end):
    MAP = [[0 for _ in range(m)] for _ in range(n)]
    need_visited, visited = [start], []
    MAP[start[0]][start[1]] = 1
    wood_point = []
    while need_visited:
        x, y = need_visited.pop()
        if (x,y) not in visited:
            visited.append((x,y))
            
            if (x,y) == end:
                return True, MAP[end[0]][end[1]], []

            for x_, y_ in move:
                if 0 <= (x+x_) < n and 0 <= (y+y_) < m:
                    if graph[x+x_][y+y_] == '0':
                        MAP[x+x_][y+y_] = MAP[x][y] + 1
                        need_visited.append((x+x_, y+y_))
                    else:
                        wood_point.append((x+x_, y+y_))
    else:
        return False, -1, wood_point


isEnd, st_count, st_point = dfs_search_road(road, start, end)
if isEnd:
    print(st_count)
else:
    _, ed_count, ed_point = dfs_search_road(road, end, start)
    intersection = list(set(st_point) & set(ed_point))
    result = []
    if intersection:
        for wood in intersection:
            tmp = copy.deepcopy(road)
            tmp[wood[0]][wood[1]] = '0'
            isBool, count, _ = dfs_search_road(tmp, start, end)
            if isBool:
                result.append(count)
        print(min(result))
    else:
        print(-1)


