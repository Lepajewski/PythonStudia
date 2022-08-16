string = input()
alfabet = "abcdefghijklmnopqrstuvwxyz"
lengths = []
which_lengths = []

string = string.lower()
for i in range(len(alfabet)):
    lengths.append(string.count(alfabet[i]))
    which_lengths.append(alfabet[i])

max_index = lengths.index(max(lengths))

print(which_lengths[max_index])
