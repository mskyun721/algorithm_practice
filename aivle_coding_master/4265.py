import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if n % 2:
    result = 0
    for i in range(n):
        tmp = list(map(int, input().split()))
        result += sum(tmp)
    
    print(result)
else:
    list_n = []
    check = []
    result = 0
    for i in range(n):
        tmp = list(map(int, input().split()))
        result += sum(tmp)
        list_n.append(tmp)

        if i % 2:
            check.append(sum(tmp[:-1]))
        else:
            check.append(sum(tmp[1:]))
        
        
    for i in range(len(list_n)-1):
        # print(i, i+1)
        if i+1 == n:
            break

        tmp1 = list_n[i]
        tmp2 = list_n[i+1]
        if i % 2 == 0:
            for j in range(m-2):
                # print(tmp1[j+2:], tmp2[:j+1])
                check.append(sum(tmp2[:j+1]) + sum(tmp1[j+2:]))
        else:
            tmp2.reverse()
            
            for j in range(m-2):
                # print(tmp1[:m-j-2], tmp2[:j+1])
                check.append(sum(tmp1[:m-j-2]) + sum(tmp2[:j+1]))

    # print(check)
    print(result - min(check))

