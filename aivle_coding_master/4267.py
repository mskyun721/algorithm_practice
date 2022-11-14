from itertools import permutations
import sys
input = sys.stdin.readline

# n : 오리배 개수 / s : 시작 번호 / m : 번호 리스트 크기
n, s, m = map(int, input().split())

boat = [i for i in range(1, n+1)]
v = list(map(int, input().split()))
cal = [1] * len(v) + [-1] * len(v)

perm = list(permutations(cal, len(cal)//2))
perm = list(set(perm))

result = 0
for p in perm:
    tmp = sum([x*y for x, y in zip(v, p)]) + s
    if tmp < n:
        result = max(result, tmp)

print(result)