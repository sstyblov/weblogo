msa = list()

file = open('example.msa', 'r')
for line in file:
    line = line.replace('\n', '')
    if line != '':
       msa.append(line)
print(msa)

length = len(msa[0])

for position in range(length):
    print(position)

