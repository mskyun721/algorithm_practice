import sys
input = sys.stdin.readline

# n = int(input())
# print((n-1)*(n-1) + 1)

n = int(input())
# for n in range(1,10):
N = 2*n
t=0

for i in range(2**N):
    c=0
    tmp = list("{0:b}".format(i).zfill(N))
    if tmp.count('0')==n:
        for j in range(len(tmp)):
            if tmp[j]=='0':
                c-=1
            else:
                c+=1
            if c<0:
                break
        else:

            print(*tmp)
            t+=1

print(t)