N = int(input())
words = []
diagonal_word = ''

for i in range(N):
    words.append(input())
    diagonal_word += words[i][i]
    
print(diagonal_word)
        
