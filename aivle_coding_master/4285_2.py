import sys
input = sys.stdin.readline

n, m = map(int,input().split())

matching = [[] for _ in range(n+1)]

mom, baby = [], []
for _ in range(m):
    m, b = map(int, input().split())
    mom.append(m)
    baby.append(b)
    matching[b].append(m)
print(matching)

baby = list(set(baby))
mom = list(set(mom))
print(min(len(baby), len(mom)))