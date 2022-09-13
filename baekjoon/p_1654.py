### 랜선 자르기 silver 2
# k : 소유한 랜선 수
# n : 필요한 랜선 수. n개 모두 같은 길이
# list : 소유한 랜선별 길이
# output : 만들 수 있는 랜선의 최대 길이

import sys
k, n = map(int, sys.stdin.readline().split())

ropes = []
for _ in range(k):
    ropes.append(int(sys.stdin.readline()))

st, end = 1, max(ropes)

while st <= end:
    mid = (st+end) // 2
    line = 0
    for i in ropes:
        line += i // mid

    if line >= n:
        st = mid+1
    else:
        end = mid-1

print(end)
