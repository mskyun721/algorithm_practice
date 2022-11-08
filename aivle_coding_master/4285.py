import sys
input = sys.stdin.readline

cnt = 0
def fn(matching, matched, end, idx=1):
    global cnt
    # print(f'idx : {idx}')

    if idx > end:
        # print('end :',matched)
        cnt = max(cnt, matched.count(False))
    else:
        # print(f'matching[idx] : {matching[idx]}')
        if matching[idx]:
            for i in matching[idx]:
                # print(f'i : {i}')
                if matched[i]:
                    matched[i] = False
                    # print(f'matched(False) : {matched}')
                    fn(matching, matched, end, idx+1)
                    matched[i] = True
                    # print(f'matched(True) : {matched}')
                else:
                    fn(matching, matched, end, idx+1)
        else:
            fn(matching, matched, end, idx+1)


n, m = map(int,input().split())

matching = {i:[] for i in range(1,n+1)}
matched = [True] * (n+1)
for _ in range(m):
    m, b = map(int, input().split())
    matching[b].append(m)

# print(matching, matched, n)
fn(matching, matched, n)
print(cnt)
