import sys
input = sys.stdin.readline

n = int(input())
list_n = list(map(int, input().split()))

bef = 1001
cnt = 0
while True:
    if len(list_n) == 0 or bef == 1:
        break
    
    if bef > max(list_n[0], list_n[-1]):
        if list_n[0] > list_n[-1]:
            bef = list_n[0]
            del list_n[0]
        else:
            bef = list_n[-1]
            del list_n[-1]
        cnt += 1
    elif bef > min(list_n[0], list_n[-1]):
        if list_n[0] > list_n[-1]:
            bef = list_n[-1]
        else:
            bef = list_n[0]
            
        del list_n[-1]
        del list_n[0]
        cnt += 1
    # elif bef < min(list_n[0], list_n[-1]):
    else:
        # break
        if len(list_n) == 1:
            break
        else:
            del list_n[0]
            del list_n[-1]
        

print(cnt)
