import sys
input = sys.stdin.readline

n, m = map(int,input().split())

matching = [[] for _ in range(n+1)]
for _ in range(m):
    m, b = map(int, input().split())
    matching[b].append(m)

# print(matching)
matching.sort(key=lambda x:-len(x))
matching = [i for i in matching if i or len(i) > 1]
matching_one = [i for i in matching if len(i) == 1]
# print(matching)

cnt = len(matching_one)
matched = [True] * (n+1)
def fn(matching, matched):
    global cnt
    tmp = matching[0]
    # print(f'tmp : {tmp}')
    for i in tmp:
        # print(f'i : {i}')
        if matched[i]:
            matched[i] = False
            # print(f'matched : {matched}')

            if len(matching) > 1:
                fn(matching[1:], matched)
            else:
                # print(f'cnt : {cnt, matched.count(False)}')
                cnt = max(cnt, matched.count(False))
                
            matched[i] = True
            # print(f'matched - True : {i, matched}')

fn(matching, matched)
print(cnt)
