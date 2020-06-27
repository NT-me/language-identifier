import identifier as idl
import os

path = 'textes/'

files = os.listdir(path)
for name in files:
    print('\n>' + name)
    file1 = open(path + name,'r')
    content1 = file1.read()
    print(idl.identifier(content1, 10))
