n = int(input())

print('2')
for i in range(3, n, 1):
    j = 2
    while j < i:
        if i % j == 0:
            break
        elif j == i - 1:
            print(i)
            break
        j+=1
        
