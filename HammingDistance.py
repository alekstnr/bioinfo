def HammingDistance(text1, text2):
    n = 0

    if len(text1) != len(text2):
        return None

    for i in range(0, len(text1)):
        if text1[i] != text2[i]:
            n += 1

    return n

#str1 = '''CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT'''
#str2 = '''CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG'''

#print(HammingDistance(str1, str2))
