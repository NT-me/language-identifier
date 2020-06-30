import timeit
import constantes

f = open("main.py", "r")
content = f.read()
print(timeit.timeit(content, number=1)/constantes.NB_ITER)
