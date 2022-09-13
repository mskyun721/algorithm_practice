### 인형들
# n : 인형의 종류
# k : 표준편차가 최소가 되는 k개 이상의 연속된 위치에 있는 인형을 같은 곳에 배치
# list : n개의 선호도

from statistics import stdev
import sys
n, k = map(int, input().split())
dolls = list(map(int, input().split()))

std = []

for i in range(k):
    std.append(stdev(dolls[i:k+i]))

print(std)
print(stdev(dolls))
