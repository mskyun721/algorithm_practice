import sys
input = sys.stdin.readline

n, m = map(int,input().split())
mom, baby = {i : [] for i in range(1,n+1)}, {i : [] for i in range(1,n+1)}

for _ in range(m):
    m, b = map(int, input().split())
    mom[m].append(b)
    baby[b].append(m)
cnt = 0

while True:
    while_bool = False
    del_mom = []
    for i in mom:
        if len(mom[i]) == 0:
            del_mom.append(i)
            continue
        elif len(mom[i]) == 1:
            b = mom[i][0]
            del_mom.append(i)
            # del baby[b]
            baby[b].remove(i)
            
            for j in mom:
                if b in mom[j]:
                    mom[j].remove(b)
            
            while_bool = True
            cnt += 1
        else:
            for j in mom[i]:
                if len(baby[j]) == 1:
                    del_mom.append(i)
                    # del baby[j]
                    baby[j].remove(i)
                    mom[i].clear()
                    
                    for k in baby:
                        if i in baby[k]:
                            baby[k].remove(i)
                    
                    while_bool = True
                    cnt += 1
                    break

    if while_bool:
        for d in del_mom:
            del mom[d]
    else:
        break

print(cnt + len(mom))