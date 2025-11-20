# Сколько существует семеричных пятизначных чисел, содержащих в своей записи ровно одну цифру 6 и не содержащих идущих подряд одинаковых цифр?
from itertools import *

count = 0
for i in product("0123456", repeat = 5):
    word = "".join(i)
    if  (word[0] != '0') and (word.count('6') == 1) and all(f"{x}{x}" not in word for x in "0123456"):
        count += 1
print(count)