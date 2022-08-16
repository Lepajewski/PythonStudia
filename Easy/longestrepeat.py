string = input() + "0"

substrings = []
l1 = []
counter = 0
max_len = ''

for i in range(len(string) - 1):
    substrings.append(string[i])
    counter += 1
    for j in range(i + 1, len(string) - 1, 1):
        if string[i] == string[j]:
            substrings[i] += string[j]
            counter += 1
        else:
            break
    i += counter
    counter = 0

for el in substrings:
    l1.append(len(el))
    if len(max_len) < len(el):
        max_len = el
    
print(max_len[0])

    
    
