### 오목 sivler 2
# 흰색 2 / 검은색 1 / 빈 칸 0
# 19*19
# ouput
# 첫번째 : 이긴 바둑 색 n
# 두번째 : 시작 위치 x, y

arr = []

for  _ in range(19):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

# move = [[1,0], [1,1], [1,-1], [-1,0]
#         , [-1,1], [-1,-1]
#         , [0,-1], [0,1]]
move = [[1,0], [1,1], [0,1], [-1, 1]]


def solution(list_arr):
    # x, y 범위 0 ~ 18
    for x in range(19):
        for y in range(19):
            if list_arr[x][y] != 0:
                go = list_arr[x][y]
                for m in move:
                    tmp = []

                    if 0 <= ((m[0] * 4) + x) < 19 and 0 <= ((m[1] * 4) + y) < 19:
                        # 기준 -1 값 확인
                        if 0 <= (x-m[0]) < 19 and 0 <= (y-m[1]) < 19:
                            if list_arr[x-m[0]][y-m[1]] == go:
                                tmp.append(list_arr[x-m[0]][y-m[1]])
                            else:
                                tmp.append(0)

                        # 기준 ~ +5 값 확인
                        tmp.append(list_arr[x][y])
                        for n in range(1, 5):
                            x_, y_ = (m[0] * n) + x, (m[1] * n) + y
                            tmp.append(list_arr[x_][y_])

                        # 기준 + 6 값 확인
                        if 0 <= ((m[0] * 5) + x) < 19 and 0 <= ((m[1] * 5) + y) < 19:
                            if list_arr[(m[0] * 5) + x][(m[1] * 5) + y] == go:
                                tmp.append(list_arr[(m[0] * 5) + x][(m[1] * 5) + y])
                            else:
                                tmp.append(0)

                        if tmp == [0, go, go, go, go, go, 0] or tmp == [go, go, go, go, go, 0] or tmp == [0, go, go, go, go, go] or tmp == [go,go,go,go,go]:
                            print(go)
                            print(x+1, y+1)
                            return True
    
    return False

result = solution(arr)

if not result:
    print(0)
