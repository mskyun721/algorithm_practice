import sys
import math
input = sys.stdin.readline

n = int(input())
list_n = []
dict_n = {}
lowser = []

winner_power = 0
winner = ''
for _ in range(n):
    name, power = input().strip().split()
    
    if winner_power < int(power):
        winner_power = int(power)
        winner = name

    list_n.append(name)
    dict_n[name] = int(power)

round = int(math.log2(n))
while True:
    total = 2**(round)

    if total == 1:
        break

    del_idx = []
    for i in range(0, total, 2):
        tmp1 = list_n[i]
        tmp2 = list_n[i+1]
        if dict_n[tmp1] > dict_n[tmp2]:
            del_idx.append(i+1)
            if winner == tmp1:
                lowser.append(tmp2)
        else:
            del_idx.append(i)
            if winner == tmp2:
                lowser.append(tmp1)
    
    del_idx.sort(reverse=True)
    for i in del_idx:
        del list_n[i]
    
    round -= 1

for i in lowser:
    print(i)