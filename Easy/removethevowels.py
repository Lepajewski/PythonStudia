string = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
output = ''
flag = False

for i in range(len(string)):
    for j in range(12):
        if string[i] == vowels[j]:
            flag = False
            break
        else:
            flag = True
    if flag == True:
        output += string[i]
            
            
print(output)
