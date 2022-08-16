l = list(map(int, input().split()))
k = int(input())

for i in range(k):
    ik, jk = map(int, input().split())
    if ik < jk:
        print(sum(l[ik:jk+1]))
    elif ik > jk:
        print(sum(l[jk:ik+1]))
    else:
        print(l[ik])
