import random as ran
import constantes
import os
# constantes

EXCLU = constantes.EXCLU
NOEXCLU = constantes.NOEXCLU

# Récupération des dico
list_dico = dict()
path = 'dict/'

files = os.listdir(path)
for file in files:
    try:
        if file.split('.')[1] == 'lang':
            file_ = open(str(path+file), ('r'))
            content_file = file_.read()
            file_.close()
            list_dico[file.split('.')[0]] = content_file.split('\n')

    except IndexError:
        # Fichier sans extension
        pass

# fileEN = open("dict/EN.txt", 'r')
# fileFR = open("dict/FR.txt", 'r')
# contentEN = fileEN.read()
# contentFR = fileFR.read()
# fileEN.close()
# fileFR.close()
# dict_EN = contentEN.split("\n")
# dict_FR = contentFR.split("\n")


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

    # On initialise le dico de note a 0 pour chaque langue
    lang_note = dict()
    for lang in list_dico:
        lang_note[lang] = 0

    for word in wordList:
        lang_find = list()

        # Recherche dans quel dictionnaire apparait le mot
        for lang in list_dico:
            if word in list_dico[lang]:
                lang_find.append(lang)

        # S'il a trouvé une langue ou plusieurs
        if len(lang_find) > 1:
            pt = NOEXCLU
        else:
            pt = EXCLU

        for flang in lang_find:
            lang_note[flang] += pt


    # Si un mot est trouvé dans un des dico la note de la langue augmente
    # for word in wordList:
    #     flag_EN = 0
    #     flag_FR = 0
    #     if word in dict_EN:
    #         flag_EN = 1
    #
    #     if word in dict_FR:
    #         flag_FR = 1
    #
    #     if flag_EN ^ flag_FR:  # Si il existe que dans UN seul des dico il prend 2
    #         if flag_EN:
    #             note_EN += EXCLU
    #         elif flag_FR:
    #             note_FR += EXCLU
    #     elif flag_EN and flag_FR:  # S'il existe dans 2 il prend que un
    #         note_EN += NOEXCLU
    #         note_FR += NOEXCLU

    # print("Note FR : " + str(note_FR))
    # print("Note EN : " + str(note_EN))

    # if note_FR > note_EN:
    #     return 'FR'
    #
    # elif note_FR < note_EN:
    #     return 'EN'
    #
    # else:
    #     return '??'

    tmp = -1
    res = ""
    for note in lang_note:
        # S'il trouve un score supérieur il le recupère
        if lang_note[note] > tmp:
            tmp = lang_note[note]
            res = note
        # S'il trouve deux fois le même rsultat alors il sors
        elif lang_note[note] == tmp:
            return '??'
    return res
