import identifier as idl
import os
import constantes
path = 'textes/'

files = os.listdir(path)
resList = dict()

NB_WORD = constantes.NB_WORD
NB_ITER = constantes.NB_ITER

for name in files:
    resList[name] = dict()
    resList[name]["EN"] = 0
    resList[name]["FR"] = 0
    resList[name]["??"] = 0

for name in files:
    # print('\n>' + name)
    file1 = open(path + name, 'r', encoding='utf_8')
    content1 = file1.read()
    for i in range(0, NB_ITER):
        print(str(i) + str(" /")+str(NB_ITER))
        lang = idl.identifier(content1, NB_WORD)
        # print(lang)
        if lang == "FR":
            resList[name]["FR"] += 1
        elif lang == "EN":
            resList[name]["EN"] += 1
        elif lang == "??":
            resList[name]["??"] += 1

with open("log.txt", "a") as logF:
    logF.write("\n")
    logF.write("NB_WORD " + str(NB_WORD) + str("\n"))
    logF.write("NB_ITER " + str(NB_ITER) + str("\n"))
    logF.write(str(resList))
