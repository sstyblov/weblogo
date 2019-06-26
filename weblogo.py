import math
import pandas as pd
import matplotlib.pyplot as plt
import dmslogo
from dmslogo.colorschemes import CBPALETTE
import string
import random
import tempfile
import urllib.request
import numpy

pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 500)

msa = list()
DNA_letters = ['A','T','C','G']
Amino_acids = ['D', 'P', 'N', 'W', 'S', 'C', 'H', 'K', 'M', 'R', 'V', 'A', 'L', 'G', 'Y', 'E', 'Q', 'I', 'F', 'T']

filename = input('Enter MSA file name: ')
file = open(filename, 'r')

for line in file:
    line = line.replace('\n', '')
    if line != '':
       msa.append(line)
print('msa', msa)

#length = len(msa[0])

positions = list(zip(*msa))
print(positions)

for position in positions:
    str = ''.join(position) #string from tuple to be able to 'count'
    #print(str.count('A'))

def entropy_DNA(positions):
    allEntropies = []
    BA_all = []
    BT_all = []
    BC_all = []
    BG_all = []
    # BA,BT,BC,BG is the height of the block at each position/column
    for position in positions:
        countA = position.count('A')
        countT = position.count('T')
        countC = position.count('C')
        countG = position.count('G')

        pA = countA/len(msa) #relative probability
        pT = countT/len(msa)
        pC = countC/len(msa)
        pG = countG/len(msa)

        HA = 0
        HT = 0
        HC = 0
        HG = 0

        if countA != 0:
            HA = -pA * math.log2(pA) #shannon entropy
        if countT != 0:
            HT = -pT * math.log2(pT)
        if countC != 0:
            HC = -pC * math.log2(pC)
        if countG != 0:
            HG = -pG * math.log2(pG)


        totH = HA + HT + HC + HG #total Entropy at each position for each nucleotid
        e = (1 / math.log(2)) * 3 / (2 * len(msa))  # approximation for the small-sample correction
                                                    #works only if number of sequences >30
        e = 0
        R = math.log2(4) - (totH + e) #Total block height at each position #(R = math.log2(4) - (totH + e))
        BA = pA * R # Block height of A
        BT = pT * R
        BC = pC * R
        BG = pG * R

        #print('R',R)
        BA_all.append(BA) #rolling over each sequence at this position
        BT_all.append(BT)
        BC_all.append(BC)
        BG_all.append(BG)
        #end of for-loop
    #end of entropy function

    #print(totalEntropy)
    allEntropies.append(BA_all)
    allEntropies.append(BT_all)
    allEntropies.append(BC_all)
    allEntropies.append(BG_all)
    print('allentropies', allEntropies)

    dataList = list()
    listToTuple = list()
    for pos in range(len(positions)):
        for DNAletter in range(len(DNA_letters)):
            listToTuple.append(pos + 1)
            listToTuple.append(DNA_letters[DNAletter])
            listToTuple.append(allEntropies[DNAletter][pos])
            dataList.append(tuple(listToTuple)) #type(dataList) = list of tuples
            listToTuple.clear()
    data = pd.DataFrame.from_records(data = dataList, columns=['site', 'letter', 'height'])
    return data


############### PROTEIN
#
# def entropy_protein(positions):
#     allEntropies_prot = []
#     #BA,BT,BC,BG is the height of the block at each position/column
#
#     B_all = []
#     countArray = []
#     probability = []
#
#     for position in positions:
#
#         for letter in Amino_acids:
#             countArray.append(position.count(letter))
#
#         for i in countArray: #array of probabilities is counted
#             probability.append(i/len(msa))
#
#         Entropy_aa = []
#         B_letter = []
#         for i in range(len(probability)): #len(probability) is always == 20
#             if countArray[i] != 0:
#                 Entropy_aa.append(-probability[i] * math.log2(probability[i]))
#
#         totH = sum(Entropy_aa) #total Entropy at each position is the sum of the entropy of all aminoacids at this one position
#         const_approx_prot = (1 / math.log(2)) * 19 / (2 * len(msa))
#         R_prot = math.log2(len(Amino_acids)) - (totH + e_prot) #the max possible height #add approximation 'e_prot' for the small-sample correction
#         B_letter = [i* R_prot for i in probability] # Blockheight of every Amino acid at one position
#
#         B_all.append(B_letter) #rolling over each position
#         countArray.clear()
#         #end of for-loop
#     #end of entropy function
#
#     #print(totalEntropy)
#     allEntropies_prot.append(B_all)
#     print('R_prot', R_prot)
#     print('allentropies', allEntropies_prot)
#
#
# ### continue with protein function:
#     dataList = list()
#     listToTuple = list()
#     for pos in range(len(positions)):
#         for DNALET in range(len(DNA_letters)):
#             listToTuple.append(pos + 1)
#             listToTuple.append(DNA_letters[DNALET])
#             listToTuple.append(allEntropies_prot[DNALET][pos])
#             dataList.append(tuple(listToTuple))
#             listToTuple.clear()
#     data = pd.DataFrame.from_records(data = dataList, columns=['site', 'letter', 'height'])
#     return data

######## END OF PROTEIN FUNCTION

S = entropy_DNA(positions)
#S = entropy_protein(positions)
fig, ax = dmslogo.draw_logo(data=S,
                            x_col = 'site',
                            letter_col = 'letter',
                            letter_height_col = 'height',
                            xlabel='position',
                            ylabel='bits')
plt.show()
with tempfile.NamedTemporaryFile(mode='wb', suffix='.png') as f:
    fig.savefig(f, dpi=450, bbox_inches='tight')

#! call prot. function