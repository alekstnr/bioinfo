from HammingDistance import HammingDistance
from itertools import product


def badneighbours(pattern, d):
    #instead of creating only what we need, we create all base-wise combinations and then limit it to what we need. this does not work well for large k.

    neighbourList = []
    k = len(pattern)

    bases = ['A', 'T', 'G', 'C']
    allBases = [''.join(base) for base in product(bases, repeat= k)]

    for base in allBases:
        if HammingDistance(pattern, base) <= d:
            neighbourList.append(base)

    return neighbourList


def neighbours(text, d):

    neighSet = {text}
    neighList = list(neighSet)
    bases = ['A', 'T', 'G', 'C']

    for dist in range(0, d):
        for pattern in neighList:
            for i in range(0, len(pattern)):
                for base in bases:
                    genString = pattern[:i] + base + pattern[i+1:]
                    neighSet.add(genString)
        neighList = list(neighSet)
    return neighSet


def recNeighbors(Pattern, d):
    if d == 0:
        return Pattern
    if len(Pattern)==1:
        return {"A", "C", "G", "T"}
    Neighborhood = []
    SuffixNeighbors = recNeighbors(Pattern[1:], d)
    for Text in SuffixNeighbors:
        if HammingDistance(Pattern[1:], Text) < d:
            for x in {"A", "C", "G", "T"}:
                Neighborhood.append(x + Text)
        else:
            Neighborhood.append(Pattern[0] + Text)
    return Neighborhood

dnalist = ["AAATTGACGCAT", "GACGACCACGTT", "CGTCAGCGCCTG", "GCTGAGCACCGG", "AGTTCGGGACAG"]
total = 0
for i in dnalist:
    total = total + len(neighbours(i, 15))
