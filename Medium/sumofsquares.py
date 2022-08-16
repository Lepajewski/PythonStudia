s = input()
print(sum(i*i for i in range(int(s[:s.index(' ')]), int(s[s.index(' '):]) + 1)))
