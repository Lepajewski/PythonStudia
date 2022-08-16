list = input().split()
i, j = input().split()
i = int(i)
j = int(j)
sum = 0

for k in range(i, j + 1, 1):
    sum += int(list[k])

print(sum)
