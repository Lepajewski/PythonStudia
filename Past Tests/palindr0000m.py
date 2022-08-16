n = input()
palindr0000mes = 0

for i in range(len(n)):
    for j in range(len(n)-i):
        number = n[j:j+i+1]
        if all(number[k] == '0' for k in range(len(number))):
            continue
        else:
            k = len(number)-1
            while number[k] == '0':
                number = number[:k]
                k -= 1
        if number == number[::-1]:
            palindr0000mes += 1
print(palindr0000mes)
        
