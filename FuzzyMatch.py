from HammingDistance import HammingDistance

def FuzzyMatch(text, pattern, d):
    matchList = []

    for i in range(0, len(text)-len(pattern)+1):
        if HammingDistance(text[i : i + len(pattern)], pattern) <= d:
            matchList.append(i)
    return matchList

def FuzzyCount(text, pattern, d):
    n = 0

    for i in range(0, len(text)-len(pattern)+1):
        if HammingDistance(text[i : i + len(pattern)], pattern) <= d:
            n += 1
    return n


Pattern = '''CCC'''
DNA = '''CATGCCATTCGCATTGTCCCAGTGA'''

#print(*FuzzyMatch(DNA, Pattern, 6))

print(FuzzyCount(DNA, Pattern, 2))
