def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count + 1
    return count

print(PatternCount("AAACATAGGATCAAC", "AA"))

def PatternAppearanceList(Text, Pattern):
    list = []
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            list.append(i)
    return list

#with open("VCholerae.txt") as text:
    #VCGenome = text.read()

#Pattern = '''ATGATCAAG'''

print(*PatternAppearanceList("AAACATAGGATCAAC", "AA"), sep=" ")
