n = int(input())
l = input().split()

for i in range(n):
    l[i] = int(l[i])

sums = []
sums.append(l[0])
temp_sum = 0

for i in range(1, len(l)):
    temp_sum += l[i]

sums.append(temp_sum)
difference = abs(sums[0] - sums[1])

for T in range(1, n):
    sums[0] = sums[0] + l[T]
    sums[1] = sums[1] - l[T]
    if abs(sums[0] - sums[1]) < difference:
        difference = abs(sums[0] - sums[1])
 
print(difference)
