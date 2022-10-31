import sys
from itertools import combinations
import copy

input = sys.stdin.readline

move = [(1,0),(0,1),(-1,0),(0,-1)]

# 동물원 크기 n*m
n, m = map(int, input().split())
zoo = [] # 동물원
bins = [] # 빈칸
jaguars = [] # 재규어 위치
jaguars_side_bin = [] # 재규어 주변 빈값

# 0 : 빈칸 / 1 : 울타리 / 2 : 재규어
for i in range(n):
    zoo.append(list(map(int, input().split())))


for x in range(n):
    for y in range(m):
        # 빈칸 위치
        if zoo[x][y] == 0:
            bins.append((x,y))

            # 빈칸 주변 재규어 유무 체크
            for t in move:
                x_, y_ = x+t[0], y+t[1]
                if (0 <= x_ < n) and (0 <= y_ < m):
                    if zoo[x_][y_] == 2:
                        jaguars_side_bin.append((x,y))
                        break
        # 재규어 위치
        elif zoo[x][y] == 2:
            jaguars.append((x,y))

# 재규어 주변 빈칸 3개 조합
comb_bin = list(combinations(jaguars_side_bin, 3))
def dfs_search_bins(graph, start):
    need_visited, visited = [start], []
    count = 0

    while need_visited:
        x, y = need_visited.pop()

        if (x,y) not in visited:
            visited.append((x,y))
            for x_, y_ in move:
                nx, ny = x+x_, y+y_
                
                if (0 <= nx < n) and (0 <= ny < m):
                    if graph[nx][ny] == 0:
                        # print(nx, ny, graph[nx][ny])
                        need_visited.append((nx, ny))
                        count += 1

    return count


result = []
for comb in comb_bin:
    tmp_zoo = copy.deepcopy(zoo)
    
    # 3개 빈칸 울타리 설치
    for point in comb:
        tmp_zoo[point[0]][point[1]] = 1
    
    # print(f'comb : {comb}')
    # print(f'tmp_zoo : {tmp_zoo}')
    # 재규어 이동 가능 빈칸 개수 확인
    count = len(bins) - 3
    for start in jaguars:
        count -= dfs_search_bins(tmp_zoo, start)
        result.append(count)


print(max(result))

                    
