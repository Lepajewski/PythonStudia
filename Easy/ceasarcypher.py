n = int(input())
message = input()
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
encrypted_message = ''

for i in range(len(message)):
    if message[i] == message[i].upper():
        encrypted_message += alphabet_upper[(alphabet_upper.index(message[i])) - n % 26]
    else:
        encrypted_message += alphabet_lower[(alphabet_lower.index(message[i])) - n % 26]

print(encrypted_message)
