N = int(input())

number_list = input().split()
flag = "NO"

for i in range(N):
    for j in range(1, N, 1):
        if abs(int(number_list[i]) - int(number_list[j])) == 1:
            flag = "YES"

print(flag)

"""
N = int(input())

number_list = input().split()
pairs = 0 #sprawdza czy istnieje wiecej niz jedna para (a, b)

for i in range(N):
    for j in range(1, len(number_list[i]), 1):
        #number_list[i] = int(number_list[i])
        if abs(int(number_list[i][j]) - int(number_list[i][j - 1])) == 1:
            pairs += 1'
                                    
if pairs == 1:
    print('YES')
else:
    print('NO')'
"""
