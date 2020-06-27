# language-identifier
Little python program for identify if a text is in french or english

## How it work
You can see an example in "main.py", but i fou want to use it you just need identifier.py and dict/*

```python
import identifier as idl # If it's in your root's project

str = "I am a string in english !"
phr = "Je suis une phrase en français !"

nb = 10 # Is the number of words on which the analysis will be based

print(idl.identifier(str, nb)) # > EN
print(idl.identifier(phr, nb)) # > FR
print(idl.identifier("fsjdkqfkjsdqlfk", nb)) # > ??
```

## Sources

Dict are from :

For French : http://infolingu.univ-mlv.fr/ under LGPLLR licence
For english : https://github.com/dwyl/english-words/ under no licence
