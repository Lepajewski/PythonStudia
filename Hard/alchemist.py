n = int(input())
values = list(map(int, input().split()))
max_val = 0
min_val = 1000
indi = 0
indj = 0
print(values)

while len(values) > 1:
    for i in range(n):
        ing1 = values[i]
        for j in range(i+1, n):
            ing2 = values[j]
            val = (ing1 + ing2) / 2
            if (ing1 + ing2) / 2 <= min_val:
                min_val = val
                indi = i
                indj = j
    print(indi, indj)
    del values[indi-1:indj]
    values.append(min_val)
    print(values)
    n -= 2
print(max_val, min_val, values)
