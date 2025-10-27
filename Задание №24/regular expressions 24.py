from re import *
line = open("24.txt").readline()

first_word = r"([A-Z][a-z]*)"
word  = r"([a-zA-Z][a-z]*)"
pattern = f"({first_word}( {word})*\.)"

print(max(len(x.group(0)) for x in finditer(pattern, line)))
