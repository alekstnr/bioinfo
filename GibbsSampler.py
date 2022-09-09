import random
import Profile as p

def weightedProbableMotif(dna, k, profile):
    #make list of all kmers
    allMotifs = [dna[i:i+k] for i in range(0, len(dna) - k + 1)]
    probList = []

    #calc list of profile-probabilities of all kmers
    for kmer in allMotifs:
        probList.append(p.Pprofile(kmer, profile))

    #choose random kmer biased on probabilities
    choice = random.choices(allMotifs, probList)

    return choice[0]

def GibbsSampler(dnalist, k, iterations):
    t = len(dnalist)
    bestMotifs = []
    motifList = []
    run = 0

    #generate initial random kmers
    for dna in dnalist:
        ranpos = random.randint(0, len(dna) - k + 1)
        motifList.append(dna[ranpos : ranpos + k])
    bestMotifs = list(motifList)

    while run <= iterations:

        #select which string to work on, initialise profile
        selection = random.randint(0, t - 1)
        prof = p.profile(k)

        #build profile excluding selection
        for i in range(0, t):
            if i != selection:
                prof.update(motifList[i])

        #choose new motif for selected line based on profile
        motifList[selection] = weightedProbableMotif(dnalist[selection], k, prof.profDict)

        #check score
        if p.score(motifList) < p.score(bestMotifs):
            bestMotifs = list(motifList)
        print(p.score(bestMotifs))

        run += 1

    print(p.score(bestMotifs))
    return bestMotifs

dnatest = [
    "CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
]

with open('dataset_163_4(1).txt', 'r') as file:
    input = file.read().strip().splitlines()
    k = int(input[0].split()[0])
    iter = int(input[0].split()[2])
    dnalist = input[1].split()


print(*GibbsSampler(dnalist, k, iter))
