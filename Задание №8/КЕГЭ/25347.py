from itertools import *

number = 0
for i in product("АГИНРТ", repeat = 6):
    word = "".join(i)
    number += 1
    if (number % 2 != 0) and (word[0] not in "АГИ") and (word.count("А") == 1):
        print(number)
        break
