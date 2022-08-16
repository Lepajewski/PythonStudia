t = int(input())

for i in range(t):
    m, n = input().split()
    m = int(m)
    n = int(n)
    if m > n:
        print(m, " is greater than ", n)
    elif m < n:
        print(m, " is smaller than ", n)
    else:
        print("n is equal m: ", m)
