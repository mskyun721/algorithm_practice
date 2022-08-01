### 게임 맵 최단거리
# 제한사항
# maps는 n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열
# n과 m은 각각 1 이상 100 이하의 자연수입니다.
# n과 m은 서로 같을 수도, 다를 수도 있지만, n과 m이 모두 1인 경우는 입력으로 주어지지 않습니다.
# maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냅니다.
# 처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.
# input
# maps = list
# output
# answer = int
def solution(maps):
    x = [-1, 1, 0, 0]
    y = [0, 0, -1, 1]

    n = len(maps)
    m = len(maps[0])

    graph = [[-1 for _ in range(m)] for _ in range(n)]
    graph[0][0] = 1

    root = [[0,0]]

    while root:
        now_y, now_x = root.pop(0)

        for i in range(4):
            move_x = now_x + x[i]
            move_y = now_y + y[i]

            if  (0 <= move_y < n) and (0 <= move_x < m) and maps[move_y][move_x] == 1:
                if graph[move_y][move_x] == -1:
                    graph[move_y][move_x] = graph[now_y][now_x] + 1
                    root.append([move_y, move_x])
            

    return graph[-1][-1]



print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
