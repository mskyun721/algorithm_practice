import sys
input = sys.stdin.readline

n, m = map(int, input().split())

result = 0
list_n = []

for i in range(n):
    tmp = list(map(int, input().split()))
    result += sum(tmp)
    list_n.append(tmp)

if n % 2:
    print(result)

else:
    check = []
    for i in range(len(list_n)-1):
        # print(i, i+1)

        tmp1 = list_n[i]
        tmp2 = list_n[i+1]
        if i % 2 == 0:
            check.append(sum(tmp1[1:]))
            # print(tmp1[1:], sum(tmp1[1:]))
            for j in range(m-2):
                # print(tmp1[j+2:], tmp2[:j+1], sum(tmp2[:j+1]) + sum(tmp1[j+2:]))
                check.append(sum(tmp2[:j+1]) + sum(tmp1[j+2:]))
        else:
            check.append(sum(tmp1[:-1]))
            # print(tmp1[:-1], sum(tmp1[:-1]))
            for j in range(m-2):
                # print(tmp1[:m-j-2], tmp2[-1-j:], sum(tmp1[:m-j-2]) + sum(tmp2[-1-j:]))
                check.append(sum(tmp1[:m-j-2]) + sum(tmp2[-1-j:]))

    # print(check)
    print(result - min(check))


