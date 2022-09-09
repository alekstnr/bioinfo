class profile:
    def __init__(self, k):
        self.k = k
        self.profDict = {"A" : [0] * self.k,
                         "C" : [0] * self.k,
                         "G" : [0] * self.k,
                         "T" : [0] * self.k}
        #Pseudocounts (laplace correction)
        self.countDict = {"A" : [1] * self.k,
                          "C" : [1] * self.k,
                          "G" : [1] * self.k,
                          "T" : [1] * self.k}
        self.colSums = [0] * self.k
        self.motifList = []

    def update(self, dna):
        self.k = len(dna)
        self.motifList.append(dna)
        self.colSums = [0] * self.k # reset column sums to 0, each update should count new

        # make count
        for pos, base in enumerate(dna):
            self.countDict[base][pos] += 1

        # make col sums
        for key, value in self.countDict.items():
            for i in range(self.k):
                self.colSums[i] += value[i]

        # make profile
        for base in self.profDict.keys():
            for i in range(self.k):
                self.profDict[base][i] = self.countDict[base][i] / self.colSums[i]

    def build(self, motifList):
        for dna in motifList:
            self.update(dna)


def profileMostProbableSet(dna, profile):
    k = len(next(iter(profile.values())))
    n = len(dna)
    probDict = {}
    maxSet = set()
    maxProb = 0
    maxKmerList = ""

    #calculating probs and adding to dict, kmer is key.
    for i in range(0, n - k + 1):
        kmer = dna[i : i + k]
        probDict.update({kmer : Pprofile(kmer, profile)})

    #sorting dict and returning set with all equally most probable kmers
    sortKeys = sorted(probDict, key=probDict.get, reverse=True)
    maxProb = probDict[sortKeys[0]]

    for key in sortKeys:
        prob = probDict[key]
        if prob >= maxProb:
            maxSet.add(key)
        else:
            break

    return maxSet


def profileMostProbable(dna, profile):
    k = len(next(iter(profile.values())))
    n = len(dna)
    maxProb = 0
    maxKmerList = []

    #calculating probs and adding to list. want to keep first maximum
    for i in range(0, n - k + 1):
        kmer = dna[i : i + k]
        prob = Pprofile(kmer, profile)
        if prob == maxProb:
            maxKmerList.append(kmer)
        elif prob > maxProb:
            maxProb = float(prob)
            maxKmerList.clear()
            maxKmerList.append(kmer)

    return maxKmerList[0]



def Pprofile(kmer, profile):
    # calculates the probability of the kmer based on profile
    p = 1

    for i, base in enumerate(kmer):
        p = p * profile[base][i]

    return p


def score(dnalist):
    k = len(dnalist[0])
    countDict = {"A" : [0] * k,
                 "C" : [0] * k,
                 "G" : [0] * k,
                 "T" : [0] * k}
    colSums = [0] * k


    for dna in dnalist:
    # make count
        for pos, base in enumerate(dna):
            countDict[base][pos] += 1

        # for score make col sums but remove largest
    for i in range(k):
        max = 0
        for base in countDict.keys():
            # go through all bases, keep track of max. when at end, minus max. (summing columns)
            num = countDict[base][i]
            if num > max:
                max = num
            colSums[i] += num
            if base == "T":
                colSums[i] -= max

    score = sum(colSums)

    return score

# profile = {
#     'A': [0.2, 0.2, 0.3, 0.2, 0.3],
#     'C': [0.4, 0.3, 0.1, 0.5, 0.1],
#     'G': [0.3, 0.3, 0.5, 0.2, 0.4],
#     'T': [0.1, 0.2, 0.1, 0.1, 0.2]
# }
#
# dna = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"

# filename = 'dataset_159_3.txt'
# with open(filename, "r") as dataset:
#     data = []
#     for line in dataset:
#         data.append(line.strip())
#     Text = data[0]
#     k = int(data[1])
#     raw_profile = data[2:]
#     bases = ['A', 'C', 'G', 'T']
#     prof = [list(map(float, raw_profile[i].split())) for i in range(len(raw_profile))]
#     profile = dict(zip(bases, prof))

def greedyMotifSearch(dnalist, k):
    t = len(dnalist)
    templatedna = dnalist[0]
    bestMotifs = [dna[0:k] for dna in dnalist]
    test = ["GAGGC", "TCATC", "TCGGC", "GAGTC", "GCAGC", "GCGGC", "GCGGC", "GCATC"]


    for i in range(0, len(templatedna) - k + 1):
        kmer = templatedna[i : i + k]
        prof = profile(k)
        prof.update(kmer)
        motifList = [kmer]

        for j in range(1, t):
            # add profile most probable to motifList, then update profile with it as well
            probableMotif = profileMostProbable(dnalist[j], prof.profDict)
            motifList.append(probableMotif)
            prof.update(probableMotif)

        if motifList ==  test:
            print("Ding")

        if score(motifList) < score(bestMotifs):
            bestMotifs = list(motifList)

    return bestMotifs

# with open('dataset_160_9.txt', 'r') as file:
#     input = file.read().strip().splitlines()
#     k = int(input[0].split()[0])
#     dnalist = input[1].split()
#
# dnatest = ["GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC", "CACGTCAATCAC", "CAATAATATTCG"]
#
# print(*greedyMotifSearch(dnalist, k))
