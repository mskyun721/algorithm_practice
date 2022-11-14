import sys
sys = sys.stdin.readline

num = int(input())
fibo = [0,0,1,2,9,44]

cnt = len(fibo)
while num > len(fibo) - 1:
    if cnt % 2 == 0:
        fibo.append(fibo[-1] * cnt + 1)
    else:
        fibo.append(fibo[-1] * cnt - 1)
    
    cnt += 1

print(fibo[num] % 10007)
    
