n = int(input())

for i in range(n):
    x = int(input())
    if x == 1:
        print('NO')
    else:
        numbs = [True for j in range(2, x)]
        for j in range(2, int(x**0.5 + 1)):
            if numbs[i]:
                for k in range(j*j, x+1, j):
                    numbs[k] = False
        if numbs[x]:
            print('YES')
        else:
            print('NO')
