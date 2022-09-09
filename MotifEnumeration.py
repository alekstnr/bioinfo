from Neighbours import neighbours

def motifenumeration(seq, k, d):
    kmerList = [set() for _ in seq]

    for pos, pattern in enumerate(seq):
        for kpos in range(0, len(pattern) - k+1):
            kmerList[pos].update(neighbours(pattern[kpos : kpos + k], d))

    finSet = kmerList[0]
    for kSet in kmerList:
        finSet = finSet & kSet

    return finSet


seqList = [
    "GGCCATTCGGTAAGCCCGATGCATA",
    "GGCGACCTATGAGCAGAGAACAGGT",
    "CGACTGCAGAAAAACGTGCCGGTCA",
    "CCGGAGTTCAGCGCCAGAGAACCAG",
    "GGACCCATGCAGGGGCGGACGACCA",
    "TTGTCACAACGATCATGGGAAATGG"
]

print(*motifenumeration(seqList, 5, 2))
