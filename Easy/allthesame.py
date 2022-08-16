n = int(input())
num = []

for i in range(n):
    x = int(input())
    num.append(x)

for i in range(n-1):
    if num[i] != num[i+1]:
        print("False")
        bool = False
        break
if bool != False:
    print("True")
    
