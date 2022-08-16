s = input()
print(sum(int(i) for i in list(s.split()) if int(i) % 2 == 0 and int(i) > 0))
