N = int(input())
numbers = []
sum = 0

numbers = input().split()

for i in range(N):
    numbers[i] = int(numbers[i])
    sum += 1.0 / numbers[i]
    
print(1.0 / sum)
