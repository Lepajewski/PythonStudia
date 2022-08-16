N = int(input())
a_n = input().split()

for i in range(N):
    a_n[i] = int(a_n[i])

a_n.sort()

for i in range(N):
    print(a_n[i], sep='', end=' ')
