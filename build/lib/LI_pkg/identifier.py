import random as ran
import constantes
# constantes

EXCLU = constantes.EXCLU
NOEXCLU = constantes.NOEXCLU

# Récupération des dico
fileEN = open("dict/EN.txt", 'r')
fileFR = open("dict/FR.txt", 'r')
contentEN = fileEN.read()
contentFR = fileFR.read()
fileEN.close()
fileFR.close()
dict_EN = contentEN.split("\n")
dict_FR = contentFR.split("\n")


def identifier(string, nb):
    """
    Return FR, EN or ??
    """
    # print("Langues chargées : FR, EN")

    # On découpe l'entrée en lexem utilisable
    input_lexe = string.split(" ")
    if nb > len(input_lexe):
        nb = len(input_lexe)

    # On choisis nb mot au piffe dedans
    wordList = set()
    for i in range(0, nb):
        wordList.add(ran.choice(input_lexe).replace("?", "").replace("!", "").replace(".", "").replace(",", "").replace(";", ""))

    note_EN = 0
    note_FR = 0

    # Si un mot est trouvé dans un des disco la note de la langue augmente
    for word in wordList:
        flag_EN = 0
        flag_FR = 0
        if word in dict_EN:
            flag_EN = 1

        if word in dict_FR:
            flag_FR = 1

        if flag_EN ^ flag_FR:  # Si il existe que dans UN seul des dico il prend 2
            if flag_EN:
                note_EN += EXCLU
            elif flag_FR:
                note_FR += EXCLU
        elif flag_EN and flag_FR:  # S'il existe dans 2 il prend que un
            note_EN += NOEXCLU
            note_FR += NOEXCLU

    # print("Note FR : " + str(note_FR))
    # print("Note EN : " + str(note_EN))

    if note_FR > note_EN:
        return 'FR'

    elif note_FR < note_EN:
        return 'EN'

    else:
        return '??'
