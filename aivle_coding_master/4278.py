import sys
input = sys.stdin.readline

n = int(input())
days = []

for i in range(n):
    day, money = map(int, input().split())
    if day+i <= n:
        tmp = [0] * (n+1)
        for j in range(i, day+i):
            tmp[j] = 1
        tmp[n] = money
        days.append(tmp)

for _ in days:
    print(_)
print()
days.sort(key=lambda x:-x[-1])

result = []
def works(must, other, score, check):
    global result
    score += must[-1]
    if True in check:
        for idx, arr in enumerate(other):
            for x, y in zip(check, arr[:-1]):
                if x == False and y == 1:
                    break
            else:
                print(f'arr : {arr}')
                for i, j in enumerate(arr[:-1]):
                    if j == 1:
                        check[i] = False

                other_ = [a for i, a in enumerate(other) if i != idx]
                works(arr, other_, score, check)

    result.append(score)


for idx, arr  in enumerate(days):
    print(f'start : {arr}')
    check = [True if j == 0 else False for j in arr[:-1]]
    other = [a for i, a in enumerate(days) if i != idx]
    works(arr, other, 0, check)
    print()
    
print(max(result))


