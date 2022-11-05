import sys

n = int(input())
list_data = []

for _ in range(n-1):
    tmp = [0] * n
    d1, d2, c, d = map(int, input().split())
    tmp[d1] = c
    tmp[d2] = d
    list_data.append(tmp)

# print(list_data)
# 최대공약수(유클리드 호제법)
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배소
def lcm(a, b):
    return a * b / gcd(a, b)

result = []
all_break = False
def data_search(data):
    global result, all_break
    tmp = []
    # print(f'data : {data}')
    if len(data) > 1:
        for idx, x in enumerate(data):
            tmp1 = x
            for idx2 in range(idx+1, len(data)):
                tmp2 = data[idx2]
                for x, y in zip(tmp1, tmp2):
                    if x != 0 and y != 0:
                        if x != y:
                            lcm_ = lcm(x, y)
                            x_, y_ = int(lcm_ // x), int(lcm_ // y)

                            tmp1_ = [(i * x_) for i in tmp1]
                            tmp2_ = [(i * y_) for i in tmp2]
                            # print(f'tmp1_ : {tmp1_}')
                            # print(f'tmp2_ : {tmp2_}')
                        else:
                            tmp1_, tmp2_ = tmp1[:], tmp2[:]

                        tmp_ = [max(i, j) for i, j in zip(tmp1_, tmp2_)]

                        if 0 not in tmp_:
                            result = tmp_
                            # print(result)
                            all_break = True

                        tmp.append(tmp_)
                        break

                if all_break:
                    break
                    
            if all_break:
                break
        
        if len(tmp) == 1 and not all_break:
            result = tmp_
        else:
            data_search(tmp)

data_search(list_data)


# print(result)
min_gcd = result[0]
for i in range(1,n):
    min_gcd = gcd(min_gcd, result[i])

for i in result:
    print(i//min_gcd, end=' ')
    

