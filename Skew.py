def Skew(text):
    skewList = [0]
    skew = 0
    for i in text:
        if i == "G":
            skew += 1
        elif i == "C":
            skew -= 1
        skewList.append(skew)
    return skewList

def minSkew(text):
    skewMap = {0 : 0}
    skew = 0
    min = 0
    minList = []

    for i in range(0, len(text)):
        if text[i] == "G":
            skew += 1
        elif text[i] == "C":
            skew -= 1
        skewMap.update({ i+1 : skew})

    sortMap = sorted(skewMap, key=skewMap.get)

    min = skewMap[sortMap[0]]

    for m in sortMap:
        if skewMap[m] == min:
            minList.append(m)
        else:
            break

    return minList

DNA = '''GATACACTTCCCGAGTAGGTACTG'''

print(*minSkew(DNA), sep=" ")
