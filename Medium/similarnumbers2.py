'''N = int(input())
number_list = list(map(int, input().split()))
flag = 'NO'

for i in range(N):
    for j in range(i + 1, N):
        #print(number_list[i], 'vs', number_list[j], '|', number_list[N - i - 2], 'vs', number_list[-j])
        if abs(number_list[i] - number_list[j]) == 1 or abs(number_list[N - i - 2] - number_list[-j]) == 1:
            flag = 'YES'
            break
    if flag == 'YES':
        break
print(flag)'''

N = int(input())
number_list = list(map(int, input().split()))

for i in number_list:
    if i+1 in number_list or i-1 in number_list:
        print('YES')
        break
    else:
        number_list.pop()
else:
    print('NO')
