from itertools import product
from FuzzyMatch import FuzzyCount
from ReverseComplement import ReverseComplement

def MaxMap(Map):
    sortMap = sorted(Map, key=Map.get, reverse=True)
    return(sortMap[0]) #returning a key

def FrequencyTable(text, k):
    freqMap = {}
    n = len(text)
    for i in range(0, n - k):
        Pattern = text[i : i + k]
        try:
            freqMap.update({Pattern : freqMap[Pattern] + 1})
        except KeyError:
            freqMap.update({Pattern : 1})
    return freqMap


def FrequentWords(text, k):
    freqList = []
    freqMap = FrequencyTable(text, k)
    max = MaxMap(freqMap) # KEY

    for string in freqMap.keys():
        if freqMap[string] == freqMap[max]:
            freqList.insert(0, string)

    return freqList


def FuzzyFrequentWords(text, k, d):
    freqMap = {}

    bases = ['A', 'T', 'G', 'C']
    allBases = [''.join(base) for base in product(bases, repeat= k)]

    for pattern in allBases:
        count = FuzzyCount(text, pattern, d)
        if count not in freqMap:
            freqMap[count] = [pattern] #the count is the key! so our freqmap now is which strings per number of fuzzy hits
        else:
            freqMap[count].insert(0, pattern)
    return freqMap[max(freqMap)]

def FuzzyFrequentWordsRC(text, k, d):
    freqMap = {}

    bases = ['A', 'T', 'G', 'C']
    allBases = [''.join(base) for base in product(bases, repeat= k)]

    for pattern in allBases:
        count = FuzzyCount(text, pattern, d) + FuzzyCount(text, ReverseComplement(pattern), d)
        if count not in freqMap:
            freqMap[count] = [pattern] #the count is the key! so our freqmap now is which strings per number of fuzzy hits plus the RC ones
        else:
            freqMap[count].append(pattern)
    return freqMap[max(freqMap)]



DNA = '''TTTTATTTTCTTTTTTTCCATATTTTTTGGCATTTCACATATAGGCATCGGTATATTTTAGGCATACAGGGGTTTTATTTTTTGGTCCACAGGTCCAGGGGTCTATATATTTTCCAGGTCTTTTTTGGTATTTTACATCGGGGCACATTTTCTCCATATCTCTATCCATATCCATATATATACAGGTCGGGGTACATCTCTATCGG'''
k = 7
d = 3

import time
start = time.process_time()
print(*FuzzyFrequentWordsRC(DNA, k, d))
print(time.process_time() - start)
