

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int,input().split())))

# 상하좌우
move = [(1,0),(0,1),(-1,0),(0,-1)]

start, end = [0,0], [n-1,m-1]
pass_count = 0
def search(graph):
    need_visited, visited = [], []
    need_visited.append(start)

    while need_visited:
        now = need_visited.pop()
        point = graph[now[0]][now[1]]

        for i in move:
            x, y = now[0]+i[0] , now[1]+i[1]
        
