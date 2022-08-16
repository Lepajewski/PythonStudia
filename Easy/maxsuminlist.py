l = input().split()
sum_max = 0
sum_temp = 0

for i in range(len(l)):
    l[i] = int(l[i])

for i in range(len(l)):
    if sum_max < 0:
        sum_max = 0
    sum_max += l[i]
    if sum_max > sum_temp:
        sum_temp = sum_max

print(sum_temp)
    
'''for i in range(1, len(l)):
    sum_temp = l[i]
    for j in range(i, len(l)):
        if l[j - 1] == l[j]:
            #print('t', sum_temp, '+=', l[j])
            sum_temp += l[j]
        else:
            break
    
    if sum_temp > sum_max:
        sum_max = sum_temp
    sum_temp = 0
if sum_max < 0:
    print(0)
else:
    print(sum_max)'''

