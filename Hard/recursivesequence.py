s = input()
for i in range(int(s[s.rfind(' ') + 1:])):
    int(s[:s.find(' ')]), int(s[s.find(' ') + 1:s.rfind(' ')]) = int(s[s.find(' ') + 1:s.rfind(' ')]), int(s[:s.find(' ')]) + int(s[s.find(' ') + 1:s.rfind(' ')])
print(int(s[:s.find(' ')]))
