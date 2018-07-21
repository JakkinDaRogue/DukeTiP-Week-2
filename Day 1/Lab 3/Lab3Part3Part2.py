def acronym(phrase):
    """
    phrase is a string, zero or more spaces
    return a string: acronym of the string
    parameter phrase
    """
    answer = ""
    phraseList = phrase.split()
    for word in phraseList:
        letter = word[0]
        answer = answer + letter
    print(answer)

acronym("Blerg's Blergnuts that Blerg")
