import math
msa = list()

file = open('example.msa', 'r')
for line in file:
    line = line.replace('\n', '')
    if line != '':
       msa.append(line)
print('msa',msa)

length = len(msa[0])

positions = list(zip(*msa))
print(positions)

# for position in positions:
#     str = ''.join(position) #string from tuple to be able to 'count'
#     print(str.count('A'))

def entropy(positions):
    totalEntropy =[]
    for position in positions:
        countA = position.count('A')
        countT = position.count('T')
        countC = position.count('C')
        countG = position.count('G')
        pA = 0
        pT = 0
        pC = 0
        pG = 0
        if countA != 0:
            pA = countA * (math.log2(countA))/4
        if countT != 0:
            pT = countT * (math.log2(countT))/4
        if countC != 0:
            pC = countC * (math.log2(countC))/4
        if countG != 0:
            pG = countG * (math.log2(countG))/4
        totalEntropy.append(pA + pT + pC + pG)
    print(totalEntropy)
    # return totalEntropy

S = entropy(positions)