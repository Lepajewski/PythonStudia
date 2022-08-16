N_of_sequences, M_of_indices = input().split()
N_of_sequences = int(N_of_sequences)
M_of_indices = int(M_of_indices)
a, b = [], []
x, y = 0, 0

sequence = input().split()

for i in range(N_of_sequences):
    sequence[i] = int(sequence[i])
for i in range(M_of_indices):
    x, y = input().split()
    a.append(int(x))
    b.append(int(y))

for i in range(M_of_indices):
    x = sequence[a[i]]
    y = sequence[b[i]]
    sequence[a[i]] = y
    sequence[b[i]] = x
    
for i in range(N_of_sequences):
    print(sequence[i], end=' ')
    
