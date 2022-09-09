from HammingDistance import HammingDistance
from itertools import product

def multiD(pattern, dnaSet):
    k = len(pattern)
    totD = 0
    maxD = k * len(dnaSet) + 1 # maximum possible score + 1 for safety
    # sum of the minimum hamming distances between pattern and any kmer in each dna string in dnaSet

    for dna in dnaSet:
        minD = maxD
        for i in range(0, len(dna) - k + 1):
            tempD = HammingDistance(pattern, dna[i : i + k])
            if tempD < minD:
                minD = tempD
        totD = totD + minD

    return totD


def medianString(dnaSet, k):
    dMap = {}
    minSet = set()

    bases = ['A', 'T', 'G', 'C']
    kmerList = [''.join(base) for base in product(bases, repeat= k)]

    for kmer in kmerList:
        d = multiD(kmer, dnaSet)
        try:
            dMap.update({kmer : dMap[kmer] + d})
        except KeyError:
            dMap.update({kmer : d})

    sortKeys = sorted(dMap, key=dMap.get)
    minDist = dMap[sortKeys[0]]

    for key in sortKeys:
        dist = int(dMap[key])
        if dist <= minDist:
            minSet.add(key)
        else:
            break

    return minSet

#pattern = "AAA"
#dnaset = {"TTACCTTAAC", "GATATCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"}

# with open("dataset_5164_1.txt") as inp:
#         input_items = inp.read().strip().splitlines()
#         pattern = input_items[0].strip()
#         dna_sequences = input_items[1].strip().split()

dna = [
    "CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC",
    "GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC",
    "GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG"
]

print(medianString(dna, 7))
