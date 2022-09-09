def ReverseComplement(text):

    reverseComp = text.maketrans("ATCG", "TAGC")

    return(text.translate(reverseComp) [::-1])

