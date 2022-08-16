str1 = input()
str1 = str1.lower()
res = 'NO'

if str1 == str1[::-1]:
    res = 'YES'
else:
    for i in range(len(str1)):
        str2 = str1[0:i] + str1[i+1::]
        if str2 == str2[::-1]:
            res = 'YES'
            break
    if res != 'YES':
        for i in range(len(str1)):
            for j in range(i+1, len(str1)):
                str2 = str1[0:i] + str1[i+1:j] + str1[j+1::]
                if str2 == '' or str2 == str2[::-1]:
                    res = 'YES'
                    break
print(res)
