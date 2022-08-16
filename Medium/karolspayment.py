t = int(input())

for i in range(t):
    a, M = map(int, input().split())
    days = 1
    total = a
    if a > M:
        days = 1
    else:
        while total <= M:
            a *= 2
            total += a
            days += 1
            print(days, a, total)
    print(days)
