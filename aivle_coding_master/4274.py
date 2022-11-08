import sys
import copy
input = sys.stdin.readline

move = [(1,0),(0,1),(-1,0),(0,-1)]
def dfs_root(MAP, st):
    visited = [st]
    cnt = [[0 for _ in range(m)] for _ in range(n)]
    check = []

    while visited:
        x, y = visited.pop()
        
        for x_, y_ in move:
            mx, my = x+x_, y+y_

            if 0 <= mx < n and 0<= my < m:
                if MAP[mx][my] == 0 and (mx, my) not in check:
                    check.append((mx, my))
                    cnt[mx][my] = cnt[x][y] + 1
                    visited.append((mx, my))

    return cnt

def transfer_tow(MAP, graph, sec):
    while sec > 0:
        sec -= 1
        tmp_MAP = copy.deepcopy(MAP)
        for x in range(n):
            for y in range(m):
                if MAP[x][y] == 0:
                    for x_, y_ in move:
                        mx, my = x+x_, y+y_
                        if 0 <= mx < n and 0 <= my < m:
                            if MAP[mx][my] == 2:
                                tmp_MAP[x][y] = 2
                                graph[x][y] = int(1e9 + 1)
                                break
        
        MAP = copy.deepcopy(tmp_MAP)
    return graph


n, m = map(int, input().split())
MAP = []
start = (-1,-1)
end = []

# 3 : 웅덩이 / 2 : 페인트 / 1 : 고양이 0 : 빈 칸
for i in range(n):
    tmp = list(map(int, input().split()))
    MAP.append(tmp)
    
    # 고양이 위치
    if start == (-1,-1):
        if 1 in tmp:
            start = (i, tmp.index(1))

    # 출구 가능 위치
    if i in [0, n-1]:
        end.extend([(i, idx) for idx, v in enumerate(tmp) if v in [0,1]])
    else:
        if tmp[0] in [0,1]:
            end.append((i, 0))
    
        if tmp[-1] in [0,1]:
            end.append((i, m-1))


if start in end:
    print(1)
elif len(end) == 0:
    print('IMPOSSIBLE')
else:
    cnt = dfs_root(MAP, start)

    max_sec = 0
    for e in end:
        max_sec = max(cnt[e[0]][e[1]], max_sec)

    if max_sec == 0:
        print('IMPOSSIBLE')
    else:
        result = transfer_tow(MAP, cnt, max_sec)
        min_sec = int(1e9)

        for e in end:
            min_sec = min(result[e[0]][e[1]], min_sec)

        if min_sec == int(1e9):
            print('IMPOSSIBLE')
        else:
            print(min_sec+1)
