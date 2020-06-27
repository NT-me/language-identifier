import random as ran

def identifier(string, nb):
    """
    Return FR, EN or ??
    """

    # Récupération des dico
    fileEN = open("dict/EN.txt",'r')
    fileFR = open("dict/FR.txt",'r')
    contentEN = fileEN.read()
    contentFR = fileFR.read()
    dict_EN = contentEN.split("\n")
    dict_FR = contentFR.split("\n")

    print("Langues chargées : FR, EN")

    # On découpe l'entrée en lexem utilisable
    input_lexe = string.split(" ")

    # On choisis nb mot au piffe dedans
    wordList = list()
    for i in range(0, nb):
        wordList.append(ran.choice(input_lexe).replace("?", "").replace("!", "").replace(".", "").replace(",", "").replace(";", ""))

    note_EN = 0
    note_FR = 0

    # Si un mot est trouvé dans un des disco la note de la langue augmente
    for word in wordList:
        if word in dict_EN:
            note_EN += 1

        if word in dict_FR:
            note_FR += 1

    print("Note FR : " + str(note_FR))
    print("Note EN : " + str(note_EN))

    if note_FR > note_EN:
        return 'FR'

    elif note_FR < note_EN:
        return 'EN'

    else:
        return '??'
