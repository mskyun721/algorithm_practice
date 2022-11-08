import sys
input = sys.stdin.readline

n = int(input())
monkeys = list(map(int, input().split()))
sum_monkeys = sum(monkeys)
total = int(input())

if total >= sum_monkeys:
    print(max(monkeys))
else:
    x = total // n

    def over_check(total, monkeys, x):
        for i in monkeys:
            if i >= x:
                total -= x
            else:
                total -= i

            if total < 0:
                return False
        else:
            return True
                
    while True:
        if over_check(total, monkeys, x):
            x += 1
        else:
            print(x-1)
            break
