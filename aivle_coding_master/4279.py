import sys
input = sys.stdin.readline

n = int(input())
list_n = list(map(int, input().split()))
lst = [0]
for idx in range(n):
    num = list_n[idx]
    if num > lst[-1]:
        lst.append(num)
    else:
        for i in range(len(lst)-2,-1,-1):
            if num > lst[i]:
                lst[i+1] = num
                break

print(n-len(lst)+1)