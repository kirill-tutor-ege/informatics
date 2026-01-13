from itertools import *

number = 0
answer = 0
for i in product("АКОРСТ", repeat = 5):
    word = "".join(i)
    number += 1
    if word[0] not in "АЛ" and word.count("С") == 1:
        answer = number
print(answer)
