import sys
input = sys.stdin.readline

n, m = map(int, input().split())
wood = []

for _ in range(n):
    wood.append(list(map(int, input().split())))

if min(n,m) < 2:
    print(0)
else:
    max_value = 0
    for i in range(n-1):
        tmp = wood[i]
        for j in range(m-1):
            tmp2 = tmp[j] + tmp[j+1]*2 + wood[i+1][j+1]
            tmp3 = tmp[j]*2 + tmp[j+1] + wood[i+1][j]
            max_tmp = max(tmp2, tmp3)

            if max_value < max_tmp:
                max_value = max_tmp
    
    for i in range(n-1, 0, -1):
        tmp = wood[i]
        for j in range(m-1):
            tmp2 = tmp[j] + tmp[j+1]*2 + wood[i-1][j+1]
            tmp3 = tmp[j]*2 + tmp[j+1] + wood[i-1][j]
            max_tmp = max(tmp2, tmp3)

            if max_value < max_tmp:
                max_value = max_tmp
    
    print(max_value)

            
