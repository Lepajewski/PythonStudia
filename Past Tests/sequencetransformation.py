length, tests = input().split()
length = int(length)
tests = int(tests)
string = input()
max_str = string

for i in range(tests):
    operation = input()
    start = int(operation[:operation.find(';')])
    end = int(operation[operation.find(';') + 1: operation.rfind(';')])
    next_sequence = operation[operation.rfind(';') + 1:]
    if start > end:
        c = end
        end = start
        start = c
    string = string[:start] + next_sequence + string[end + 1:]
    
    if len(string) >= len(max_str):
        max_str = string
        
print(string)
print(max_str)
