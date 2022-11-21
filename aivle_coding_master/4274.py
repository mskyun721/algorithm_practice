from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
start = tuple()
end = []
paint = []
graph = []
# 3 : 웅덩이 / 2 : 페인트 / 1 : 고양이 0 : 빈 칸
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    
    for idx, j in enumerate(tmp):
        # 고양이 위치
        if j == 1:
            start = (i,idx)
        # 페인트 위치
        elif j == 2:
            paint.append((i,idx))

    # 출구 위치
    if i in [0, n-1]:
        end.extend([(i, idx) for idx, v in enumerate(tmp) if v in [0,1]])
    else:
        if tmp[0] in [0,1]:
            end.append((i, 0))
    
        if tmp[-1] in [0,1]:
            end.append((i, m-1))


MAP = [[[0,0]for _ in range(m)] for _ in range(n)]
move = [(1,0),(0,1),(-1,0),(0,-1)]
def search(graph, start):
    need_visited = deque()
    need_visited.append(start)

    while need_visited:
        x, y = need_visited.popleft()

        for x_, y_ in move:
            dx, dy = x+x_, y+y_
            if 0 <= dx < n and 0 <= dy <m:
                if graph[dx][dy] == 0:
                    if MAP[dx][dy][0] == 0 or MAP[dx][dy][0] > (MAP[x][y][0]+ 1):
                        MAP[dx][dy][0] = MAP[x][y][0] + 1
                        if MAP[dx][dy][0] < MAP[dx][dy][1]:
                            need_visited.append((dx,dy))


def expasion(graph, start):
    need_visited = deque()
    need_visited.append(start)

    while need_visited:
        x, y = need_visited.popleft()

        for x_, y_ in move:
            dx, dy = x+x_, y+y_
            if 0 <= dx < n and 0 <= dy < m:
                if graph[dx][dy] == 0 or graph[dx][dy] == 1:
                    if MAP[dx][dy][1] == 0 or MAP[dx][dy][1] > (MAP[x][y][1] + 1):
                        MAP[dx][dy][1] = MAP[x][y][1] + 1
                        need_visited.append((dx,dy))
                        
    
if start in end:
    print(1)
elif len(end) == 0:
    print('IMPOSSIBLE')
else:
    for p in paint:
        expasion(graph, p)

    search(graph, start)
    
    for i in MAP:
        print(i)

    result = []
    for e in end:
        if MAP[e[0]][e[1]][0] < MAP[e[0]][e[1]][1] and MAP[e[0]][e[1]][0] > 0:
            result.append(MAP[e[0]][e[1]][0] + 1)

    if result:
        print(min(result))
    else:
        print('IMPOSSIBLE')
