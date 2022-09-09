import random
import Profile as prof

#random.seed(4)

def randomMotifSearchIter(dnalist, k, runs):
    t = len(dnalist)
    motifList = []
    bestMotifs = []
    finalMotifs = [dna[0 : k] for dna in dnalist]

    run = 0

    while run <= runs:

        #picking random kmers
        for dna in dnalist:
            ranpos = random.randint(0, len(dna) - k + 1)
            motifList.append(dna[ranpos : ranpos + k])
        bestMotifs = list(motifList)


        searching = True

        while searching:
            #make profile from random motif list
            profile = prof.profile(k)
            profile.build(motifList)

            #build new motif list from profile
            motifList.clear()
            for dnastr in dnalist:
                motifList.append(prof.profileMostProbable(dnastr, profile.profDict))

            #check if score is better in inside loop
            if prof.score(motifList) < prof.score(bestMotifs):
                bestMotifs = list(motifList)
            else:
                searching = False

        #check if score is better in outside loop
        if prof.score(bestMotifs) < prof.score(finalMotifs):
            finalMotifs = list(bestMotifs)



        run += 1

    return finalMotifs

dnatest = [
    "GCACATCATTAAACGATTCGCCGCATTGCCTCGATTAACC",
    "TCATAACTGACACCTGCTCTGGCACCGCTCATCCAAGGCC",
    "AAGCGGGTATAGCCAGATAGTGCCAATAATTTCCTTAACC",
    "AGTCGGTGGTGAAGTGTGGGTTATGGGGAAAGGCAAGGCC",
    "AACCGGACGGCAACTACGGTTACAACGCAGCAAGTTAACC",
    "AGGCGTCTGTTGTTGCTAACACCGTTAAGCGACGAAGGCC",
    "AAGCTTCCAACATCGTCTTGGCATCTCGGTGTGTTTAACC",
    "AATTGAACATCTTACTCTTTTCGCTTTCAAAAAAAAGGCC",
]

with open('dataset_161_5.txt', 'r') as file:
    input = file.read().strip().splitlines()
    k = int(input[0].split()[0])
    dnalist = input[1].split()


print(*randomMotifSearchIter(dnalist, k, 1000))
