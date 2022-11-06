import sys
input = sys.stdin.readline

n = int(input())

zip = []
wifi = []
for i in range(n):
    tmp = list(map(int, input().split()))
    tmp_zip = [(i, j) for j in range(n) if tmp[j] == 1]
    tmp_wifi = [(i, j) for j in range(n) if tmp[j] == 2]
    zip.extend(tmp_zip)
    wifi.extend(tmp_wifi)

result = int(sys.maxsize)
for x, y in wifi:
    dist = 0
    for x_, y_ in zip:
        dist += (abs(x - x_) + abs(y - y_))
    
    result = min(result, dist)

print(result)
