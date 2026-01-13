from itertools import *

number = 0 
for i in product("АКОРСТ", repeat = 5):
    number += 1
    word = "".join(i)
    if  (number % 2 == 0) and\
        (word[0] not in "АСТ") and\
        (word.count("О") == 2):
        print(number)
