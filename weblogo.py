msa = list()

file = open('example.msa', 'r')
for line in file:
    line = line.replace('\n', '')
    if line != '':
       msa.append(line)
print(msa)

length = len(msa[0])

positions = list(zip(*msa))

for position in positions:
    str = ''.join(position)
    print(str.count('A'))
