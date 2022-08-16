h = int(input())
n = int(input())

for i in range(n):
    for j in range(h):
        print('* ' * (j+1))
    h += 1
