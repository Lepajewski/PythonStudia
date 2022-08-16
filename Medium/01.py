text = list(input().split())

for i in range(len(text)):
    text[i] = int(text[i], 2)
    text[i] = chr(text[i])
    print(text[i], end='')
