a = input()
b = input()

for i in range(len(a) // 2 + 1):
    #print(a[0:i] + a[i+1:], '|', a[0:len(a) - i] + a[len(a) - i + 1:])
    if a[0:i] + a[i+1:] == b or a[0:len(a) - i] + a[len(a) - i + 1:] == b:
        print('TAK')
        break
else:
    print('NIE')

