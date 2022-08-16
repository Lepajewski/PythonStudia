n = int(input())
squares = [int(i) for i in input().split()]
maks_tmp = 0
maks = 0

for i in range(n):
    for j in range(i + 1, n):
        if squares[i] >= squares[j]:
            maks_tmp += 1
        else:
            break
        i += 1
    if maks < maks_tmp:
        maks = maks_tmp
    maks_tmp = 0

print(maks)



