# (№ 7546) (ЕГЭ-2024) Определите количество 14-ричных пятизначных чисел, в записи которых ровно одна цифра 9 
# и не более трех цифр с числовым значением, превышающим 10.
from itertools import *

count = 0
for i in product("0123456789ABCD", repeat = 5):
    word = "".join(i)
    if word[0] != '0' and word.count('9') == 1 and (word.count("B") + word.count("C") + word.count("D") <= 3):
        count += 1
print(count)
