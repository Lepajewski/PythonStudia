n = int(input())

for i in range(n):
    s = input()
    tmp = ''
    for j in range(1, len(s)):
        if s[j] == '+':
            print(s[:j], '|', s[j+1:])
            tmp = s[:j] + ' + ' + s[j+1:]
    print(tmp)
    print(s)
        
    left, right = s.split('=')
    right = right.split('+')
    left = left.split('+')
    #print(left, right)
