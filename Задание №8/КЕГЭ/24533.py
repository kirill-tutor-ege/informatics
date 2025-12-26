from itertools import *

answer = 0
number = 0
for i in product("АЕКНОТ", repeat = 7):
    word = "".join(i)
    number += 1
    if  (number % 2 != 0) and\
        (word.count("Е") == 1 and word.count("К") == 2 and word.count("Н") == 1 and word.count("О") == 2 and word.count("Т") == 1):
        answer = number
print(answer)
