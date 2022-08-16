s = input()
print(True if all([int(s) % i != 0 for i in range(2, int(s) // 2 + 1)]) else False)
